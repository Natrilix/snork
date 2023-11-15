from turtle import Turtle

FONT = ('Courior', 24, 'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.hideturtle()
        self.write(arg=f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!", font=FONT, align=ALIGNMENT)
