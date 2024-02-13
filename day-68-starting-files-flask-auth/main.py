from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user_email = str(request.form.get("email"))
        the_user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()
        if the_user:
            flash("this email is already in the db please try another one or log in")
            return redirect(url_for("login"))
        else:
            the_password = generate_password_hash(request.form.get("password"), method="pbkdf2:sha256", salt_length=8)
            new_user = User(
                email=str(request.form.get("email")), password=str(the_password),
                name=str(request.form.get("name")))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("login"))

    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_email = str(request.form.get("email"))
        the_user = db.session.execute(db.select(User).where(User.email == user_email)).scalar()
        if the_user:
            user_login_password = str(request.form.get("password"))
            user_password = the_user.password
            password_true = check_password_hash(user_password, user_login_password)
            if password_true:
                login_user(the_user)
                return redirect(url_for("secrets", user_id=the_user.id))
            else:
                flash("wrong password")
        else:
            flash("this email does not exist in the db")
    return render_template("login.html")


@app.route('/secrets/')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route('/download')
@login_required
def download():
    name = "files/cheat_sheet.pdf"
    return send_from_directory(app.static_folder, name)



if __name__ == "__main__":
    app.run(debug=True)
