from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# TODO: Create a snake body
segment_1 = Turtle(shape="square")
segment_1.color("white")

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(-20,0)

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(-40,0)

# TODO: How to move the snake
# TODO: Control the snake
# TODO: Detect collision with food
# TODO: Create a scoreboard
# TODO: Detect collision with wall
# TODO: Detect collision with tail

screen.exitonclick()