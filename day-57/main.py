from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/43e3b809cdcf1eef9e41").json()
all_post_objects = []
for post in posts:
    p = Post(
        post_id=post["id"],
        post_title=post["title"],
        post_subtitle=post["subtitle"],
        post_body=post["body"])
    all_post_objects.append(p)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_post_objects)


@app.route("/post/<int:post_num>")
def get_post(post_num):
    return render_template("post.html", post=all_post_objects[post_num-1])


if __name__ == "__main__":
    app.run(debug=True)
