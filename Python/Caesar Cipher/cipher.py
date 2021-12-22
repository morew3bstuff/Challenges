# Inport
from lettersModule import *
from artModule import *

print(logo)

# User input
direction = input("""Type "encode" to encode your message and "decode" to decode youe message: """).lower()
text = input(f"""Message to be {direction.upper()}: """)
shift = int(input("Type the shift number: "))

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for char in start_text:
        if char in letters:
            position = letters.index(char)
            new_position = position + shift_amount
            end_text += letters[new_position]
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}.")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)