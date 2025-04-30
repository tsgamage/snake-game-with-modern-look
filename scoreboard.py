from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("courier", 24, "bold")
GAME_OVER_FONT = ("courier", 24, "normal")
REASON_FONT = ("courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self, text_color = "white"):
        super().__init__()
        self.hideturtle()
        self.color(text_color)
        self.penup()
        self.goto(0, 305)
        self.score = 0
        self.increase_score()

    def show_score(self):
        self.write(f"Score: {self.score}", move=False, align=TEXT_ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.show_score()
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align=TEXT_ALIGNMENT, font=GAME_OVER_FONT)

    def game_over_reason(self, reason="Please give a reason"):
        self.goto(0, -20)
        self.color("red")
        self.write(reason, move=False, align=TEXT_ALIGNMENT, font=REASON_FONT)