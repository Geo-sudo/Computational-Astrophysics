from Binary_Star_System import BinarySystem, Star

binary_system = BinarySystem(width=1400, height=900)

star1 = Star(binary_system, mass=5000, position=(0,0), velocity=(0,0))
star2 = Star(binary_system, mass=100, position=(-500,0), velocity=(0,2), color="white")


while True:
    binary_system.gravity_baby(star1,star2)
    binary_system.update_all()