import random
from turtle import Turtle,Screen
import time
from food import Food
from scorebord import ScoreBord

import snake
from snake import Snake

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scorebord=ScoreBord()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#dettect snake is hit or not
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorebord.update_score()

    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        game_is_on=False
        scorebord.walltouch()













screen.exitonclick()








