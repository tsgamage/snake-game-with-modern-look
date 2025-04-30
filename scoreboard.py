from turtle import Turtle

TEXT_ALIGNMENT = "center"
FONT = ("courier", 24, "bold")
GAME_OVER_FONT = ("courier", 24, "normal")
REASON_FONT = ("courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self, text_color="white"):
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

    def black_box(self):
        game_over_turtle = Turtle()
        game_over_turtle.hideturtle()
        game_over_turtle.penup()

        game_over_turtle.goto(-125, -50)  # adjust to fit the text background
        game_over_turtle.color("black")
        game_over_turtle.begin_fill()
        for _ in range(2):
            game_over_turtle.forward(250)  # width of rectangle
            game_over_turtle.left(90)
            game_over_turtle.forward(100)  # height of rectangle
            game_over_turtle.left(90)
        game_over_turtle.end_fill()

    def game_over(self):
        self.black_box()
        self.goto(0, -10)
        self.color("White")
        self.write("GAME OVER", move=False, align=TEXT_ALIGNMENT, font=GAME_OVER_FONT)

    def game_over_reason(self, reason="Please give a reason"):
        self.goto(0, -30)
        self.color("red")
        self.write(reason, move=False, align=TEXT_ALIGNMENT, font=REASON_FONT)

