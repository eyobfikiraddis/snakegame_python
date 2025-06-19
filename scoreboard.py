from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
with open("../../../Desktop/python projects/snake game/highscore.txt", mode = "r") as file:
    x = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.highscore = int(x)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode = "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
