from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.post import PostCreate, PostResponse
from services.post_services import add_post, get_user_posts, delete_post
from services.auth_services import verify_token
from database import SessionLocal
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/addpost")
def add_post_endpoint(post: PostCreate, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    user_id = token['user_id']
    new_post = add_post(db, user_id, post.text)
    return {"id": new_post.id, "text": new_post.text}

@router.get("/getposts")
def get_posts_endpoint(token: str = Depends(verify_token), db: Session = Depends(get_db)):
    user_id = token['user_id']
    posts = get_user_posts(db, user_id)
    return [{"id": post.id, "text": post.text} for post in posts]

@router.delete("/deletepost")
def delete_post_endpoint(post_id: int, token: str = Depends(verify_token), db: Session = Depends(get_db)):
    if delete_post(db, post_id):
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="Post not found")
