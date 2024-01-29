from turtle import Turtle
MOVE_DISTANCE = 20
DIRECTIONS = {"RIGHT":0, "UP": 90, "LEFT": 180, "DOWN": 270}


class Snake:
    def __init__(self):
        self.segments = []
        for i in range(3):
            self.add_segment((-MOVE_DISTANCE * i, 0))
        self.head = self.segments[0]

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            previous_segment = self.segments[segment_index - 1]
            self.segments[segment_index].goto(previous_segment.xcor(), previous_segment.ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DIRECTIONS["DOWN"]:
            self.head.setheading(DIRECTIONS["UP"])

    def down(self):
        if self.head.heading() != DIRECTIONS["UP"]:
            self.head.setheading(DIRECTIONS["DOWN"])

    def left(self):
        if self.head.heading() != DIRECTIONS["RIGHT"]:
            self.head.setheading(DIRECTIONS["LEFT"])

    def right(self):
        if self.head.heading() != DIRECTIONS["LEFT"]:
            self.head.setheading(DIRECTIONS["RIGHT"])

    def add_segment(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
