from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake(Turtle):
    def __init__(self):
        self.snake_list = []
        self.x = 0
        self.create()

    def create(self):
        for a in range(0, 3):
            new_snake = Turtle(shape="square")
            new_snake.color("white")
            new_snake.penup()
            new_snake.goto(self.x, 0)
            self.x -= 20
            self.snake_list.append(new_snake)

    def extend(self):
        new_snake = Turtle(shape="square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(self.snake_list[-1].position())
        self.snake_list.append(new_snake)

    def move(self):
        for num in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[num - 1].xcor()
            new_y = self.snake_list[num - 1].ycor()
            self.snake_list[num].goto(new_x, new_y)
        self.snake_list[0].forward(20)

    def reset(self):
        for body in self.snake_list:
            body.goto(1000, 1000)
        self.snake_list.clear()
        self.create()

    def up(self):
        if self.snake_list[0].heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.snake_list[0].heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def left(self):
        if self.snake_list[0].heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def right(self):
        if self.snake_list[0].heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)
