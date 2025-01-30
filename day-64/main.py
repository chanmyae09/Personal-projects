from idlelib.squeezer import Squeezer

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from werkzeug.exceptions import NotFound
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

url = "https://api.themoviedb.org/3/search/movie"
api_access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OGYyN2U4N2E0MzI0NGM1NTRiZmViOGUwN2QyNGVlYyIsIm5iZiI6MTczODEyODM1MS43MzQwMDAyLCJzdWIiOiI2Nzk5YmJkZmIwOTM1OWU1Y2NhOTZjZDkiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.y2r8OCfOTxCkjgtr2FSSlSdeBMfKbgv_6k8j_ogyXgE"

header = {
    "accept": "application/json",
    "Authorization": f"Bearer {api_access_token}"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

class Form(FlaskForm):
    rating = StringField("Your rating out of 10. eg.7.5")
    review = StringField("Your review")
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    movie = StringField("Movie Title",validators=[InputRequired()])
    submit = SubmitField("Add Movie")

# CREATE DB
class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-movives.db"

db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()  # convert ScalarResult to Python List
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html",movies= all_movies)


@app.route("/edit",methods = ["GET","POST"])
def edit():
    form = Form()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',form=form,movie=movie)


@app.route("/delete")
def delete():
    movie_id= request.args.get("id")
    movie = db.get_or_404(Movie,movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add",methods=["GET","POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        params = {
            "query": form.movie.data
        }
        response = requests.get(url, headers=header, params=params)
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template('add.html',form = form)

@app.route("/find")
def find_movie():
    movie_api_id= request.args.get("id")
    if movie_api_id:
        link = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        response= requests.get(url=link, headers= header)
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit",id= new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
