from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserLogin
from models.user import User
from services.auth_services import create_access_token
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def create_user(db: Session, user_data: UserCreate):
    user = User(**user_data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    if not db_user.verify_password(user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
    
    access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}