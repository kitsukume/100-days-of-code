alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def encrypt(direction, text, shift):
    message = ""
    if direction == "encode":
        for letter in text:
            numbers = (alphabet.index(letter))
            shifted = (numbers + shift) %26
            encoded = alphabet[shifted]
            message += encoded
        print(message)
    elif direction == "decode":
        for letter in text:
            numbers = (alphabet.index(letter))
            shifted = (numbers - shift) %26
            encoded = alphabet[shifted]
            message += encoded
        print(message)
    else:
        print("Invalid choice")

direction = input("Type encode or decode to encrypt or decrypt your message.\n")
text= input("Type your message:\n")
shift = int(input("How many your want to shift:\n"))

encrypt(direction, text, shift)