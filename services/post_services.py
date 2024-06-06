from sqlalchemy.orm import Session
from models.post import Post

def add_post(db: Session, user_id: int, text: str):
    new_post = Post(text=text, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_user_posts(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()

def delete_post(db: Session, post_id: int):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
        return True
    return False