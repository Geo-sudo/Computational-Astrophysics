import math
from Vectors import Vector
import matplotlib.pyplot as plt
import scipy.constants as sci

class BinarySystem:
    def __init__(self, size):
        self.size = size
        self.bodies = []
        
        self.fig, self.ax = plt.subplots(1, 1, subplot_kw={"projection":"3d"}, figsize=(self.size/50, self.size/50))
        self.fig.tight_layout()
        self.ax.view_init(0, 0)
        
    def add_body(self,body):
        self.bodies.append(body)

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()

    def draw_all(self):
        self.ax.set_xlim([-self.size/2, self.size/2])
        self.ax.set_ylim([-self.size/2, self.size/2])
        self.ax.set_zlim([-self.size/2, self.size/2])
        plt.pause(0.001)
        self.ax.clear()
    
    def calc_gravity(self):
        for it, first in enumerate(self.bodies):
            for second in self.bodies[it+1:]:
                first.acc_due_to_gravity(second)

class Body:
    min_display_size = 10
    display_log_base = 1.3

    def __init__(self, binary_system: BinarySystem, mass, position=(0,0,0), velocity=(0,0,0), colour="black"):
        self.binary_system = binary_system
        self.mass = mass
        self.position = Vector(*position)
        self.velocity = Vector(*velocity)
        self.display_size = max(
            math.log(self.mass, self.display_log_base),
            self.min_display_size
        )
        self.colour = colour

        self.binary_system.add_body(self)

    def move(self):
        self.position = (
            self.position[0] + (self.velocity[0]),
            self.position[1] + (self.velocity[1]),
            self.position[2] + (self.velocity[2])
        )
    
    def draw(self):
        self.binary_system.ax.plot(
            *self.position,
            marker="o",
            markersize=self.display_size,
            color=self.colour
        )
    
    def acc_due_to_gravity(self, other):
        r = Vector(*other.position) - Vector(*self.position)
        r_norm = r.get_norm()

        force_norm = self.mass * other.mass / (r_norm**2)
        force = r.normalize() * force_norm
        
        reverse = 1
        for body in self, other:
            acc = force/body.mass
            body.velocity += acc * reverse
            reverse = -1

