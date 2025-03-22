# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount):
    if direction == "encode".lower():
        cipher_text = ""

        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
        print(f"Here is the encoded result: {cipher_text}")

    elif direction == "decode".lower():
        cipher_text = ""

        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_positions = alphabet.index(letter) - shift_amount
                shifted_positions %= len(alphabet)
                cipher_text += alphabet[shifted_positions]
        print(f"Here is the decoded result: {cipher_text}")


# TODO-3: Can you figure out a way to restart the cipher program?

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type anything else to exit:\n").lower()
    if "encode".lower() != direction != "decode".lower():
        print("---Thanks for playing!---")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift)



