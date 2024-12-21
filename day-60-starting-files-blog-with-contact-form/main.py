import os
import smtplib

from flask import Flask, render_template, request
import requests

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

my_email = os.environ["MY_EMAIL"]
my_password = os.environ["MY_PASSWORD"]


@app.route('/')
def get_all_posts():
    print(my_email)
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        msg = request.form["name"] + "\n" + request.form["email"] + "\n" + request.form["phone"] + "\n" + request.form["message"]
        encoded_msg = msg.encode('utf-8')
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=request.form["email"], to_addrs=my_email, msg=encoded_msg)
        print(request.form["name"] + "\n" + request.form["email"] + "\n" + request.form["phone"] +
              "\n" + request.form["message"])
        return render_template("contact.html", main_h1="Successfully send your msg!")
    else:
        return render_template("contact.html", main_h1="Contact Me!")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
