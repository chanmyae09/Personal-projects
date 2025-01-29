from turtle import Turtle

FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-250,250)
        self.write(self.level, align="center", font=FONT)

    def player_point(self):
        self.level+=1
        self.update_score()


