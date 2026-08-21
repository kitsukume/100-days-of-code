import random

vocab = ["朝", "家", "車", "エンジン", "綺麗"]
meaning =["morning", "house", "car", "engine", "beautiful"]

r_position = random.randint(0, len(vocab)-1)

answer = input(f"What does {vocab[r_position]} mean?\n")

if answer == meaning[r_position]:
    print("correct")
else:
    print("incorrect")