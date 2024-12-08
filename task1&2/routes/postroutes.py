'''post api controller'''
from database import SessionLocal
from models import User, Post

def create_posts():
    """create posts by id user"""
    db = SessionLocal()
    posts = [
        Post(title="Post 1", content="Content1", user_id=1),
        Post(title="Post 2", content="Content2", user_id=2),
    ]
    db.add_all(posts)
    db.commit()
    db.close()

def get_all_posts_users():
    """find all posts with user"""
    db = SessionLocal()
    posts = db.query(Post, User).join(User, Post.user_id == User.id).all()
    results = [
            {
                "post_id": post.id,
                "title": post.title,
                "content": post.content,
                "user": {
                    "user_id": user.id,
                    "username": user.username,
                    "email": user.email
                }
            }
            for post, user in posts
        ]
    db.close()
    return results

def get_posts_by_user(user_id: int):
    """find posts by user id"""
    db = SessionLocal()
    posts = db.query(Post).filter(Post.user_id == user_id).all()
    results = [
        {
            "post_id": post.id,
            "title": post.title,
            "content": post.content
        }
        for post in posts
    ]
    db.close()
    return results
        
def update_post_content(post_id: int, new_content: str):
    """update content by post id"""
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    post.content = new_content
    db.commit()
    db.close()

def delete_post(post_id: int):
    """delete post by post id"""
    db = SessionLocal()
    post = db.query(Post).filter(Post.id == post_id).first()
    db.delete(post)
    db.commit()
    db.close()
