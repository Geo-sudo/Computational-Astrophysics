from Vectors import Vector
import matplotlib.pyplot as plt
import math


class BinarySystem:
    def __init__(self, size, dt):
        self.size = size
        self.dt = dt #in years
        self.bodies = []

        self.fig, self.ax = plt.subplots(1,1,subplot_kw={"projection": "3d"}, figsize=(self.size, self.size))
        self.fig.tight_layout()

        self.ax.set_xlim([0, self.size])
        self.ax.set_ylim([0, self.size])
        self.ax.set_zlim([0, self.size])

    def add_body(self, body):
        self.bodies.append(body)
    
class Body:
    min_display_size = 10
    display_log_base = 1.3

    def __init__(self, binary_system, mass, position=(0,0,0),velocity=(0,0,0)):
        self.binary_system = binary_system
        self.mass = mass
        self.position = position
        self.velcotiy = Vector(*velocity)
        self.display_size(max(math.log(self.mass, self.display_log_base), self.min_display_size))
        self.colour = "black"

        self.binary_system.add_body(self)

    def move(self):
        self.position = (self.position[0] + self.velcotiy[0]*self.binary_system.dt, self.position[1] + self.velcotiy[1]*self.binary_system.dt, self.posittion[2] + self.velcotiy[2]*self.binary_system.dt)

