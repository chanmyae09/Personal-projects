import turtle
import turtle as t
import random

color = ["red", "green", "blue", "yellow", "purple", "orange", "pink",]
screen = t.Screen()
screen.setup(width =500,height = 400)
user_bet = screen.textinput(title = "Make your bet",prompt = "Which turtle will win the race? Enter a color:")
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []
for turtle_index in range(0,6):
    turtle = t.Turtle(shape='turtle')
    turtle.penup()
    turtle.color(color[turtle_index])
    turtle.goto(x=-230,y = y_positions[turtle_index])
    all_turtles.append(turtle)

if user_bet:
    is_race_on =True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!")
            else:
                print(f"You've lost")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()