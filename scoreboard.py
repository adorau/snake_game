from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.pencolor("white")
        self.write(f"Score: {self.point} ", False, align="center", font=("Calibre", 14, "normal"))

    def add_point(self):
        self.clear()
        self.point += 1
        self.write(f"Score: {self.point} ", False, align="center", font=("Calibre", 14, "normal"))

    def game_over_print(self):
        self.goto(0,0)
        self.write("GAME OVER :( ", False, align="center", font=("Calibre", 14, "normal"))
