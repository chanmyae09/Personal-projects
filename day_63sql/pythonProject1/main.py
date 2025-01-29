# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///new-books-collection.db"
db.init_app(app)

class Book(db.Model):
  id:Mapped[int] = mapped_column(Integer,primary_key=True)
  title:Mapped[str] = mapped_column(String(250),nullable=False,unique=True)
  author:Mapped[str] = mapped_column(String(250),nullable=False)
  rating:Mapped[int] = mapped_column(Float,nullable=False)

  def __repr__(self):
    return f"<Book(title='{self.title}',author = '{self.author}', rating={self.rating})>"

with app.app_context():
  db.create_all()

with app.app_context():
  book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter and the Chamber of Secrets J. K. Rowling")).scalar()

  if not book:
    new_book = Book(id=2, title="Harry Potter and the Chamber of Secrets J. K. Rowling", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
    print(new_book)
  else:
    # book.rating = 9.0
    # db.session.commit()
    print(book)









