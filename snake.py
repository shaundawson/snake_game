from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# TODO: Create a snake body
# segment_1 = Turtle(shape="square")
# segment_1.color("white")

# segment_2 = Turtle(shape="square")
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3 = Turtle(shape="square")
# segment_3.color("white")
# segment_3.goto(-40,0)

class Snake:

    
    def __init__(self):
        self.segments = []
        self.create_snake()

    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    # TODO: Animate the snake segments to move forward
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
