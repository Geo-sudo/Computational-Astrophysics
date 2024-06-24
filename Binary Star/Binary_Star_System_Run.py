from Binary_Star_System import BinarySystem, Star

binary_system = BinarySystem(width=1400, height=900)

star1 = Star(binary_system, mass=500000, position=(500,-30), velocity=(0.1,0.2))
star2 = Star(binary_system, mass=10000, position=(-50,10), velocity=(0.1,-0.3), color="white")

while True:
    binary_system.update_all()