import matplotlib.pyplot as plt
from Binary_System import BinarySystem, Body

binary_system = BinarySystem(400)

body = Body(binary_system, 100, velocity=(1,1,1))

for _ in range(100):
    binary_system.update_all()
    binary_system.draw_all()