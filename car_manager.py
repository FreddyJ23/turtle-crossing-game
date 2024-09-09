from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.create_cars(10,100, 400)
        self.hideturtle()

    def create_cars(self, num, position_x, position_y):
        for new_car in range(num):
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.pu()
            new_car.goto(random.randint(position_x, position_y), random.randint(-250, 250))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE
            new_y = car.ycor()
            car.goto(new_x, new_y)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT


