"""user api controller"""
from database import SessionLocal
from models import User, Post

def create_users():
    """Added users in tables"""
    db = SessionLocal()
    users = [
        User(username="user1", email="user1@example.com", password="password1"),
        User(username="user2", email="user2@example.com", password="password2"),
    ]
    db.add_all(users)
    db.commit()
    db.close()

def get_all_users():
    """get all users"""
    db = SessionLocal()
    users = db.query(User).all()
    for u in users:
        print(f"{u.email}, {u.username}, {u.id}")
    db.close()
    return users

def update_user_email(user_id: int, new_email: str):
    """update email by user id"""
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    user.email = new_email
    db.commit()
    db.close()

def delete_user_and_posts(user_id: int):
    """delete all user and all him posts"""
    db = SessionLocal()
    db.query(Post).filter(Post.user_id == user_id).delete()
    user = db.query(User).filter(User.id == user_id).first()
    db.delete(user)
    db.commit()
    db.close()