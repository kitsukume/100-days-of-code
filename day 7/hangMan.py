import random
import wordList
import art


print("Welcome to a fun game of Hangman")

guessed = []
r_word = random.choice(wordList.words)
n_letter = len(r_word)


guess_list = []
point = 0

for letter in r_word:
    guess_list.append("_")
print(art.HANGMANPICS[0])
print("_" * n_letter)
while "_" in guess_list and point < 6  :
    


    u_choice = input("select a letter: ")


    if u_choice in guessed:
                print("guessed")
                continue
    guessed.append(u_choice)  
    for position, letter in enumerate(r_word):

        if u_choice == letter :
            
            guess_list[position] = letter
        
    if u_choice not in r_word:
            point += 1
    print(art.HANGMANPICS[point])
    string = ""       
    for letter in guess_list:
        string += letter
    print(string)
      

 
    if "_" not in guess_list:
            print("you win")
    elif point == 6 :
        print("gameover.")



            
