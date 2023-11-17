import math

def kmh_to_mps(velocity):
    return velocity/3.6

def velocity_decomposition(velocity, angle):
    alpha = math.radians(angle)
    horizontal_velocity = velocity * math.cos(alpha)
    vertical_velocity = velocity * math.sin(alpha)
    return horizontal_velocity, vertical_velocity

def airtime(vertical_velocity, init_height, g = 9.81):
    return (vertical_velocity + math.sqrt(vertical_velocity ** 2 + 2 * g * init_height))/g


def throw_distance(angle, velocity, init_height=1.8):

       
    mps = kmh_to_mps(velocity)
    horizontal_velocity, vertical_velocity = velocity_decomposition(mps, angle)

    distance = horizontal_velocity * airtime(vertical_velocity, init_height)

    print(f"""
    Velocity in m/s: {mps}
    Horizontal velocity: {horizontal_velocity}
    Vertical velocity: {vertical_velocity}
    Airtime: {airtime(vertical_velocity, init_height)}
    Distance thrown: {distance:.2f}
    """)

angle_input = float(input("Enter angle in degrees: "))
velocity_input = float(input("Enter velocity in km/h: "))
init_height_input = float(input("Input initiation height: "))

