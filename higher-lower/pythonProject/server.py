from flask import Flask
import random
app = Flask(__name__)

rand_num= random.randint(0,9)
print(rand_num)

@app.route('/')
def number_guesser():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src= 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>")

@app.route('/<int:guess>')
def guess_number(guess):
    if guess> rand_num:
        return "<h1 style='color: #002aff'>Too high, try again</h1>"
    elif guess< rand_num:
        return "<h1 style='color: #ffbaba'>Too low, try again</h1>"
    else:
        return "<h1 style='color: #00ff00'>It's correct!</h1>"


if __name__ == "__main__":
    app.run(debug=True)