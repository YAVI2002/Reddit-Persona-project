import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent="persona-generator"
    )

def fetch_user_data(username, limit=50):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    comments = [f"[Comment] {comment.body}\n[Permalink] https://reddit.com{comment.permalink}" for comment in user.comments.new(limit=limit)]
    posts = [f"[Post] {post.title}\n{post.selftext}\n[Permalink] https://reddit.com{post.permalink}" for post in user.submissions.new(limit=limit)]

    return {"comments": comments, "posts": posts}
