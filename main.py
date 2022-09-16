from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
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

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_list[0].distance(food) < 15:
        food.refresh()
        scoreboard.refresh()
        snake.extend()

    if snake.snake_list[0].xcor() > 300 or snake.snake_list[0].xcor() < -300 or snake.snake_list[0].ycor() > 300 or snake.snake_list[0].ycor() < -300:
        scoreboard.reset()
        snake.reset()

    for body in snake.snake_list[1:]:
        if snake.snake_list[0].distance(body) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()