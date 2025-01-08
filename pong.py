import turtle as t 

class Paddle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("black")
        self.speed(0)
        self.shapesize(stretch_wid=6, stretch_len=2)

class Ball(t.Turtle):
    pass

class Game():
    def __init__(self):
        sc = t.screen()
        sc.title("Pong Game")
        sc.bgcolor("white")
        sc.setup(width = 1000, height = 1000)

    def run(self):
        pass