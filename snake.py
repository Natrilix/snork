from turtle import Turtle

UP_DIRECTION = 90
DOWN_DIRECTION = 270
LEFT_DIRECTION = 180
RIGHT_DIRECTION = 0

class Snake:
    MOVE_DISTANCE = 20
    SEGMENT_SIZE = 20
    INITIAL_SNAKE_LENGTH = 3

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.snake_head = self.snake_segments[0]

    def create_snake(self):
        for i in range(0, self.INITIAL_SNAKE_LENGTH):
            self.create_segment(x_pos=0-i*self.SEGMENT_SIZE, y_pos=0)

    def create_segment(self, x_pos, y_pos):
        snake_piece = Turtle()
        snake_piece.shape("square")
        snake_piece.color("yellow", "green")
        snake_piece.penup()
        snake_piece.setx(x_pos)
        snake_piece.sety(y_pos)
        self.snake_segments.append(snake_piece)

    def grow_snake(self):
        self.create_segment(self.snake_segments[-1].xcor(), self.snake_segments[-1].ycor())

    def move(self):
        for i in reversed(range(1, len(self.snake_segments))):
            self.snake_segments[i].setx(self.snake_segments[i - 1].xcor())
            self.snake_segments[i].sety(self.snake_segments[i - 1].ycor())
        self.snake_head.forward(self.MOVE_DISTANCE)

    def up(self):
        if self.snake_head.heading() != DOWN_DIRECTION:
            self.snake_head.setheading(UP_DIRECTION)
        else:
            pass

    def right(self):
        if self.snake_head.heading() != LEFT_DIRECTION:
            self.snake_head.setheading(RIGHT_DIRECTION)
        else:
            pass
    def down(self):
        if self.snake_head.heading() != UP_DIRECTION:
            self.snake_head.setheading(DOWN_DIRECTION)
        else:
            pass

    def left(self):
        if self.snake_head.heading() != RIGHT_DIRECTION:
            self.snake_head.setheading(LEFT_DIRECTION)
        else:
            pass
