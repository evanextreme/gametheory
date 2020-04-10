# Simple Snake Game in Python 3 for Beginners
# By @TokyoEdTech
# from Gist https://gist.githubusercontent.com/wynand1004/ec105fd2f457b10d971c09586ec44900/raw/f6c27fb821b67131d2ba52cd6e1bcc430f2c0dbc/snake_game.py

import os
import turtle
import time
import random
from playsound import playsound


class SnakeGame():

    # Functions

    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"

    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"

    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"

    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"

    def move(self):
        if self.head.direction == "up":
            y = self.head.ycor()
            self.head.sety(y + 20)

        if self.head.direction == "down":
            y = self.head.ycor()
            self.head.sety(y - 20)

        if self.head.direction == "left":
            x = self.head.xcor()
            self.head.setx(x - 20)

        if self.head.direction == "right":
            x = self.head.xcor()
            self.head.setx(x + 20)

    def __init__(self, high_score=30):
        self.delay = 0.1

        self.score = 0
        self.high_score = high_score
        # Set up the screen
        self.wn = turtle.Screen()
        self.wn.title(
            "Welcome to Game Theory, the greatest ransomware in gameing")
        self.wn.bgcolor("green")
        self.wn.setup(width=600, height=600)
        self.wn.tracer(0)  # Turns off the screen updates

        # Snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color("black")
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"

        # Snake food
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color("red")
        self.food.penup()
        self.food.goto(0, 100)

        self.segments = []

        # Pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)

        self.pen.write("Your files are gone :))).",
                       align="center", font=("Courier", 24, "normal"))

        # playsound(os.path.join(os.path.split(
        #    __file__)[0], "audio", "intro.wav"))
        self.pen.clear()
        self.pen.write("Beat the high score to get them back.",
                       align="center", font=("Courier", 24, "normal"))
        time.sleep(4)
        self.pen.clear()
        self.pen.write("Close this window and lose them forever.",
                       align="center", font=("Courier", 24, "normal"))
        time.sleep(4)
        self.pen.clear()
        self.pen.write("Use (WASD) to play.", align="center",
                       font=("Courier", 24, "normal"))
        # Keyboard bindings
        self.wn.listen()
        self.wn.onkeypress(self.go_up, "w")
        self.wn.onkeypress(self.go_down, "s")
        self.wn.onkeypress(self.go_left, "a")
        self.wn.onkeypress(self.go_right, "d")

        # Main game loop
        while True:
            self.wn.update()

            # Check for a collision with the border
            if self.head.xcor() > 290 or self.head.xcor() < -290 or \
                    self.head.ycor() > 290 or self.head.ycor() < -290:
                time.sleep(1)
                self.head.goto(0, 0)
                self.head.direction = "stop"

                # Hide the segments
                for segment in self.segments:
                    segment.goto(1000, 1000)

                # Clear the segments list
                self.segments.clear()

                # Reset the score
                self.score = 0

                # Reset the delay
                self.delay = 0.1

                self.pen.clear()
                self.pen.write("Score: {}  High Score: {}".format(
                    self.score, self.high_score),
                    align="center", font=("Courier", 24, "normal"))

            # Check for a collision with the food
            if self.head.distance(self.food) < 20:
                # Move the food to a random spot
                x = random.randint(-290, 290)
                y = random.randint(-290, 290)
                self.food.goto(x, y)

                # Add a segment
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                self.segments.append(new_segment)

                # Shorten the delay
                self.delay -= 0.001

                # Increase the score
                self.score += 10

                if self.score > self.high_score:
                    self.high_score = self.score
                    self.pen.clear()

                    self.pen.write("You did it!! Decrypting files...",
                                   align="center",
                                   font=("Courier", 24, "normal"))
                    # playsound(os.path.join(os.path.split(
                    #    __file__)[0], "audio", "outro.wav"))

                    self.wn.bye()
                    break

                self.pen.clear()
                self.pen.write("Score: {}  High Score: {}".format(
                    self.score, self.high_score), align="center",
                    font=("Courier", 24, "normal"))

            # Move the end segments first in reverse order
            for index in range(len(self.segments)-1, 0, -1):
                x = self.segments[index-1].xcor()
                y = self.segments[index-1].ycor()
                self.segments[index].goto(x, y)

            # Move segment 0 to where the self.head is
            if len(self.segments) > 0:
                x = self.head.xcor()
                y = self.head.ycor()
                self.segments[0].goto(x, y)

            self.move()

            # Check for head collision with the body segments
            for segment in self.segments:
                if segment.distance(self.head) < 20:
                    time.sleep(1)
                    self.head.goto(0, 0)
                    self.head.direction = "stop"

                    # Hide the segments
                    for segment in self.segments:
                        segment.goto(1000, 1000)

                    # Clear the segments list
                    self.segments.clear()

                    # Reset the score
                    self.score = 0

                    # Reset the delay
                    self.delay = 0.1

                    # Update the scozre display
                    self.pen.clear()
                    self.pen.write("Score: {}  High Score: {}".format(
                        self.score, self.high_score),
                        align="center", font=("Courier", 24, "normal"))

            time.sleep(self.delay)
