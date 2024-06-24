import turtle
import math

class BinarySystemBody(turtle.Turtle):
    minDisplaySize = 20
    displayLogBase = 1.1

    def __init__(self, Binary_System, mass, position=(0,0), velocity=(0,0)):
        super().__init__()
        self.mass=mass
        self.setposition(position)
        self.velocity = velocity
        self.display_size = max(math.log(self.mass, self.displayLogBase), self.minDisplaySize)

        self.penup()
        self.hideturtle()

        Binary_System.addBody(self)
    
    def draw(self):
        self.clear()
        self.dot(self.display_size)
    def move(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])

class Star(BinarySystemBody):
    def __init__(self, Binary_System, mass, position=(0,0), velocity=(5,0), color="blue"):
        super().__init__(Binary_System, mass, position, velocity)
        self.color(color)


class BinarySystem:
    def __init__(self, width, height):
        self.Binary_System = turtle.Screen()
        self.Binary_System.tracer(0)
        self.Binary_System.setup(width,height)
        self.Binary_System.bgcolor("black")

        self.bodies = []
    def addBody(self, body):
        self.bodies.append(body)
    def removeBody(self, body):
        self.bodies.remove(body)
    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
            self.Binary_System.update()
    