'''main.py'''
from database import engine, Base
from routes.postroutes import create_posts, get_all_posts_users, get_posts_by_user, update_post_content, delete_post
from routes.userroutes import create_users, get_all_users, update_user_email, delete_user_and_posts


if __name__ == "__main__":
    try:
        Base.metadata.create_all(bind = engine) # step 1 create tables
        print("migration do it")
        try:
            create_users() # step 2 create users
        except Exception:
            print("Такие пользователи уже существуют")
        create_posts() # step 2 create posts
        get_all_users() # step 2 get all users

        posts_with_users = get_all_posts_users() # step 2 get all posts with user
        for post in posts_with_users:
            print(post)
        user_id = 1
        try:
            user_posts = get_posts_by_user(user_id) # step 2 get all posts by user id
            for post in user_posts:
                print(post)
        except Exception:
            print("User id not exist")
        try:
            update_user_email(2, "1@1.1") # step 2 update email by user id
        except Exception:
            print("User not found")
        get_all_users()
        try:
            update_post_content(1, "NEW CONTENT") # step 2 update posts by posts id
        except Exception:
            print("posts not found")
        try:
            delete_post(2) # step 2 delete post by post id
        except Exception:
            print("post was deleted")
        delete_user_and_posts(2) # step 2 delete user with him posts
    except Exception:
        print("program error")

