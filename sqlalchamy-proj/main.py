# import sqlite3
#
# db = sqlite3.connect("book-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books "
# #                "(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, "
# #                "author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

from flask import Flask
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    author: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)


with app.app_context():
    db.create_all()

# create a new record
with app.app_context():
    new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()

# read all records
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    print(all_books)

# read a particular record by query
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()

# update a particular record by query
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

# delete a particular record
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()