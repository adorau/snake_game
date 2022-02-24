from turtle import Turtle, Screen
from food import Food
from scoreboard import Scoreboard
import time


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.setup_screen()
        self.turtle = Turtle()
        self.food = Food()
        self.body = []
        self.point = 0

        self.setup_body()
        self.scoreboard = Scoreboard()

    def setup_screen(self):
        self.screen.setup(width=600, height=600)
        self.screen.cv._rootwindow.resizable(False, False)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.screen.listen()

    def setup_body(self):
        new_segment = self.add_segment(-0, 0)
        self.body.append(new_segment)
        new_segment = self.add_segment(-20, 0)
        self.body.append(new_segment)
        new_segment = self.add_segment(-40, 0)
        self.body.append(new_segment)

    def add_segment(self, x, y):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.setx(x)
        segment.sety(y)
        return segment

    def start_game(self):
        on_game = True

        while on_game:
            self.screen.update()
            time.sleep(0.18)

            for segment in range(len(self.body) - 1, 0, -1):
                x = self.body[segment - 1].xcor()
                y = self.body[segment - 1].ycor()
                self.body[segment].goto(x, y)
            self.body[0].forward(20)
            self.screen.listen()
            self.screen.onkey(self.up, "Up")
            self.screen.onkey(self.down, "Down")
            self.screen.onkey(self.right, "Right")
            self.screen.onkey(self.left, "Left")
            self.screen.onkey(self.quit_game, "q")

            if self.body[0].distance(self.food) < 15:
                self.food.go_to_the()
                x_pos_last_segment = self.body[len(self.body) - 1].xcor()
                y_pos_last_segment = self.body[len(self.body) - 1].ycor()
                new_segment = self.add_segment(x_pos_last_segment, y_pos_last_segment)
                self.body.append(new_segment)
                self.scoreboard.add_point()

            if self.body[0].xcor() < -300 or self.body[0].xcor() > 280 \
                        or self.body[0].ycor() < -280 or self.body[0].ycor() > 300:
                self.scoreboard.game_over_print()
                on_game = False
            for seg in range(len(self.body) - 1, 1, -1):
                if self.body[0].distance(self.body[seg]) < 10:
                    self.scoreboard.game_over_print()
                    on_game = False

        self.close_screen()

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def quit_game(self):
        self.screen.bye()

    def close_screen(self):
        self.screen.exitonclick()
