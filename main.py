from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
FPS = 15

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snork")
screen.tracer(0)

#Snake.SNAKE_LENGTH = 9
snake = Snake()

screen.listen()
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.up, "Up")

food = Food()
scoreboard = Scoreboard()

playing = True
while playing:
    screen.update()
    time.sleep(1/FPS)
    snake.move()

    #Detect collisions
    #With food
    if snake.snake_head.distance(food) < 15:
        food.new_location()
        scoreboard.score_up()
        snake.grow_snake()

    #With walls
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280
            or snake.snake_head.ycor() >280 or snake.snake_head.ycor() < -280):
        scoreboard.game_over()
        playing = False

    #With tail
    for segment in snake.snake_segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.game_over()
            playing = False

screen.exitonclick()
