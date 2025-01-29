from flask import Flask, render_template, request_tearing_down
import random
import datetime
import requests

gender_url="https://api.genderize.io"
age_url = "https://api.agify.io"
params = {'name': 'michael'}


app = Flask(__name__)
@app.route("/")
def home():
    random_number = random.randint(0,9)
    year = datetime.datetime.now().year
    return render_template('index.html',num=random_number,year = year)


@app.route("/guess/<name>")
def guess(name):
    age_response = requests.get(url=age_url, params={'name':name}).json()['age']
    gender_response = requests.get(url=gender_url, params={'name': name}).json()['gender']
    return render_template('guess.html',age = age_response,gender = gender_response,person_name = name)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html',posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)

