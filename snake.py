import time
from turtle import Turtle, Screen

screen = Screen()
screen.addshape(r"assets\images\snake-body.gif")
screen.addshape(r"assets\images\head-right.gif")
screen.addshape(r"assets\images\head-left.gif")
screen.addshape(r"assets\images\head-down.gif")
screen.addshape(r"assets\images\head-up.gif")

SNAKE_POSITIONS = [(-40, 0), (-20, 0), (0, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, color="white"):
        self.segments = []
        self.snake_color = color
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in SNAKE_POSITIONS:
            is_it_head = False

            if position == SNAKE_POSITIONS[0]:
                is_it_head = True

            self.add_segment(position, is_it_head)

    def add_segment(self, position, is_it_head=False):
        segment = Turtle()
        if is_it_head:
            segment.shape(r"assets\images\head-right.gif")
        else:
            segment.shape(r"assets\images\snake-body.gif")
        segment.color(self.snake_color)
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend_a_segment(self):
        last_segments_position = self.segments[-1].position()
        self.add_segment(last_segments_position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].shape(r"assets\images\head-up.gif")
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].shape(r"assets\images\head-down.gif")
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.segments[0].shape(r"assets\images\head-left.gif")

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].shape(r"assets\images\head-right.gif")
            self.head.setheading(RIGHT)
