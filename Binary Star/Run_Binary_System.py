import matplotlib.pyplot as plt
from Binary_System import BinarySystem, Body

binary_system = BinarySystem(1000)

star1 = Body(binary_system, 500000)
star2 = Body(binary_system, 50, position=(50,0,500), velocity=(0,25,5))

while True:
    binary_system.calc_gravity()
    binary_system.update_all()
    binary_system.draw_all()
