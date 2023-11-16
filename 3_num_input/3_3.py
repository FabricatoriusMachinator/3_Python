import math

angle = float(input("Enter angle in degrees: "))
velocity = float(input("Enter velocity in km/h: "))
init_height = float(input("Input initiation height: "))

alpha = math.radians(angle)
mps = velocity/3.6
horizontal_velocity = mps * math.cos(alpha)
vertical_velocity = mps * math.sin(alpha)

airtime = (vertical_velocity + math.sqrt(vertical_velocity ** 2 + 2 * 9.81 * init_height))/9.81
distance = horizontal_velocity * airtime

print(f"""
    Alpha: {alpha}
    Velocity in m/s: {mps}
    Horizontal velocity: {horizontal_velocity}
    Vertical velocity: {vertical_velocity}
    Airtime: {airtime}
    Distance thrown: {distance:.2f}
""")
