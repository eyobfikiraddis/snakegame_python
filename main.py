from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

x = 0.15

while True:
    screen.update()
    time.sleep(x)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        x *= 0.95

    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        snake.head.goto(snake.head.xcor() * -1,snake.head.ycor())
    elif snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(), snake.head.ycor() * -1)

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





screen.exitonclick()
