import random
from turtle import Turtle, Screen
import numpy as np
import itertools

apple_1 = r"assets\images\apple_ani\7.gif"
apple_2 = r"assets\images\apple_ani\6.gif"
apple_3 = r"assets\images\apple_ani\5.gif"
apple_4 = r"assets\images\apple_ani\4.gif"
apple_5 = r"assets\images\apple_ani\3.gif"
apple_6 = r"assets\images\apple_ani\2.gif"
apple_7 = r"assets\images\apple_ani\1.gif"

apple_pngs = itertools.cycle([apple_1, apple_2, apple_3, apple_4, apple_5, apple_6, apple_7])

screen = Screen()
screen.addshape(r"assets\images\apple.gif")
screen.addshape(apple_1)
screen.addshape(apple_2)
screen.addshape(apple_3)
screen.addshape(apple_4)
screen.addshape(apple_5)
screen.addshape(apple_6)
screen.addshape(apple_7)


def floor_to_preferred(number, preferred):
    return np.floor(number / preferred) * preferred


def random_even():
    random_number = random.randint(-250, 250)
    random_number = floor_to_preferred(random_number, 20)
    return random_number


class Food(Turtle):

    def __init__(self, color="green"):
        super().__init__()
        self.shape(r"assets\images\apple.gif")
        self.color(color)
        self.penup()
        self.speed("fastest")
        self.goto(random_even(), random_even())

    def refresh(self):
        def animate():
            frame = next(apple_pngs)
            self.shape(frame)
            if frame != apple_7:
                screen.ontimer(animate, 50)

        animate()
        self.goto(random_even(), random_even())
