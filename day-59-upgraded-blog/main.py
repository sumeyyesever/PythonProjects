from flask import Flask, render_template
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/dc9f154ab2e20a896a18").json()
print(posts)


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def get_post(post_id):
    the_post = {}
    for post in posts:
        if post["id"] == post_id:
            the_post = post
    return render_template("post.html", post=the_post)


if __name__ == "__main__":
    app.run(debug=True)