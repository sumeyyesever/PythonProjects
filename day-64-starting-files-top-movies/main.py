from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests


HEADERS = {
        "accept": "application/json",
        "Authorization": ""
}


class MyForm(FlaskForm):
    rating = StringField('Your Rating Out of 10', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField("Done")


class MyForm2(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///films-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[str] = mapped_column(nullable=True)
    img_url: Mapped[str] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for movie in all_movies:
        movie.ranking = len(all_movies) - all_movies.index(movie)
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = MyForm2()
    if request.method == "POST":
        url = "https://api.themoviedb.org/3/search/movie"
        headers = HEADERS
        params = {
            "query": form.title.data
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        the_list = data["results"]
        return render_template("select.html", movies_list=the_list)

    return render_template("add.html", form=form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
    image_url = "https://image.tmdb.org/t/p/w500"
    headers = HEADERS
    response = requests.get(url, headers=headers)
    data = response.json()
    movie = Movie(title=data["original_title"], year=data["release_date"],
                  description=data["overview"], img_url=f"{image_url}{data['poster_path']}", rating=0, ranking=0,
                  review="")
    db.session.add(movie)
    db.session.commit()
    return redirect(url_for("edit", id=movie.id))


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = MyForm()
    movie = db.get_or_404(Movie, id)
    if request.method == "POST":
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form)


@app.route("/delete/<int:id>")
def delete(id):
    movie = db.get_or_404(Movie, id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
