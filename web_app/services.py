"""business function app"""
from sqlalchemy.orm import Session
from models import User, Post

# Users
def get_users(db: Session):
    """Get all users"""
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    """Get user by ID"""
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, username: str, email: str, password: str):
    """Create a new user"""
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def update_user(db: Session, user_id: int, username: str, email: str):
    """Update user information"""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        user.email = email
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int):
    """Delete user and their posts"""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.query(Post).filter(Post.user_id == user.id).delete()  # Delete user's posts
        db.delete(user)
        db.commit()
    return user

# Posts
def get_posts(db: Session):
    """Get all posts"""
    return db.query(Post).all()

def get_post_by_id(db: Session, post_id: int):
    """Get post by ID"""
    return db.query(Post).filter(Post.id == post_id).first()

def create_post(db: Session, title: str, content: str, user_id: int):
    """Create a new post"""
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def update_post(db: Session, post_id: int, title: str, content: str, user_id: int):
    """Update post information"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        post.title = title
        post.content = content
        post.user_id = user_id
        db.commit()
        db.refresh(post)
    return post

def delete_post(db: Session, post_id: int):
    """Delete post by ID"""
    post = db.query(Post).filter(Post.id == post_id).first()
    if post:
        db.delete(post)
        db.commit()
    return post
