from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("blue")
        self.head.shape("triangle")

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)
        # turtle.degrees(360)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color("blue")
        self.head.shape("triangle")

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 90.0 and self.segments[0].heading() != 270.0:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90.0 and self.segments[0].heading() != 270.0:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 0.0 and self.segments[0].heading() != 180.0:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 180.0 and self.segments[0].heading() != 0.0:
            self.segments[0].setheading(180)
