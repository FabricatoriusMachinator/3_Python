import keyboard 

def handle_input(var1, var2):
    print(f"""
Press the following to choose operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """)

    while True:
        if keyboard.is_pressed('1'):
            print(f"Result of the addition: {var1 + var2}")
            break
        if keyboard.is_pressed('2'):
            print(f"Result of the subtraction: {var1 - var2}")
            break
        if keyboard.is_pressed('3'):
            print(f"Result of the multiplicaiton: {var1 * var2}")
            break
        if keyboard.is_pressed('4'):
            print(f"Result of the division: {var1 / var2}")
            break

inpt1 = float(input("Type in value 1: "))
inpt2 = float(input("Type in value 2: "))

handle_input(inpt1,inpt2)

