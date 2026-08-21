#Independent result before course solution
import random

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "?", "."]

print("Welcome to the PyPassword Generator.")
nr_letters = int(input("how many letters would you like in your password?\n"))
nr_cap_letters = int(input("How many capital letters would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

r_letters = random.choices(letters, k=nr_letters)
r_cap_letter = random.choices(capital_letters, k=nr_cap_letters)
r_symbol = random.choices(symbols, k=nr_symbols)
r_number = random.choices(numbers, k=nr_numbers)

l_password = r_letters+r_cap_letter+r_symbol+r_number
random.shuffle(l_password)

password = ""

for char in l_password:
    password += char
    
print(password)