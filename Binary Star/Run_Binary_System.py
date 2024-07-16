import matplotlib.pyplot as plt
from Binary_System import BinarySystem, Body
from matplotlib.animation import FuncAnimation

#Unit are in AU, M0, and days

t=0 # <--- Run for how many days

binary_system = BinarySystem(50, 1500)

#Sirius  

#Sirius_A = Body(binary_system, 2.063, 0.007952299, position=(-5.958,0,0), velocity=(0.0000702,-0.0000702,0), colour="blue", set_size=True, size=25)
#Sirius_B = Body(binary_system, 1.018, 3.720374e-5, position=(14.042,0,0), velocity=(-0.0000458,0.0000458,0), colour="cyan", set_size=True, size=25)


#Random numbers that worked

star1 = Body(binary_system, 1, 4.6491e-3, colour="blue", set_size=True, size=25)
star2 = Body(binary_system, 3.003e-6, 4.2588e-5, position=(1,0,1), velocity=(0,0.000172,0), colour="yellow", set_size=True, size=15)

"""
# Saving Aniamtion:
# A bit buggy
def animate(n):
    binary_system.calc_gravity()
    binary_system.update_all()
    binary_system.draw_all()
    return binary_system.ax.artists

anim = FuncAnimation(fig = binary_system.fig, func = animate, frames = 240, interval = 100, repeat = True)
anim.save('A.mp4',fps=24, dpi=300)
"""


# Testing Animation:

while t < 100000000:
    binary_system.calc_gravity()
    binary_system.update_all()
    binary_system.draw_all()
    t += binary_system.dt
