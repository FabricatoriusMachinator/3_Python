captured = ("Pikachu", "Pidgey", "Abra", "Pidgey", "Eevee", "Pidgey")

captured_set = set(captured)

user_input = input("Type in a Pokémon: ")

if user_input in captured_set:
    print(f"Ash has captured {user_input}.")
else:
    print(f"Ash has not captured {user_input}.")
