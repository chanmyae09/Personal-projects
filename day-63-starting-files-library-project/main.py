from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)


class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)
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

@app.route('/')
def home():
    with app.app_context():
        # Query all books from the database
        all_books = db.session.query(Book).all()

    return render_template("index.html",books=all_books)


@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        new_book = Book(title=request.form["title"],
                                author=request.form["author"], rating=request.form["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/edit/<id>",methods=['GET', 'POST'])
def edit(id):
    if request.method=="POST":
        book_to_update = db.session.execute(db.select(Book).where(Book.id == int(id))).scalar()
        book_to_update.rating=request.form.get("changed_rating")
        db.session.commit()
        return redirect(url_for("home"))
    else:
        with app.app_context():
            book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            return render_template("edit.html",book= book)







if __name__ == "__main__":
    app.run(debug=True)

