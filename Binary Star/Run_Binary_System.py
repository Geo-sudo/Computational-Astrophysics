import matplotlib.pyplot as plt
from Binary_System import BinarySystem, Body

#Unit are in AU, M0, and days

t=0

binary_system = BinarySystem(2.5, 200)

star1 = Body(binary_system, 1, 4.6491e-3, colour="blue", set_size=True, size=25)
star2 = Body(binary_system, 3.003e-6, 4.2588e-5, position=(1,0,1), velocity=(0,0.000172,0), colour="yellow", set_size=True, size=15)

while t < 100000:
    binary_system.calc_gravity()
    binary_system.update_all()
    binary_system.draw_all()
    t += binary_system.dt
