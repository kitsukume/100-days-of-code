alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

def ceaser(direction, text, shift):
    message = ""
    if direction == "encode":
        for letter in text:
            if letter in alphabet:
                numbers = (alphabet.index(letter))
                shifted = (numbers + shift) %26
                encoded = alphabet[shifted]
                message += encoded
            else:
                message += letter
        print(message)
    elif direction == "decode":
        for letter in text:
            if letter in alphabet:
                numbers = (alphabet.index(letter))
                shifted = (numbers - shift) %26
                encoded = alphabet[shifted]
                message += encoded
            else:
                message += letter
        print(message)
    
direction= ""
while direction  != "exit":
    direction = input("Type encode, decode or exit to encrypt or decrypt your message or to exit program.\n")
    if direction == "exit":
        break
    text = input("Type your message:\n")
    shift = int(input("How many your want to shift:\n"))


    ceaser(direction, text, shift)
