print("Welcome to name\n make it to end for loots")
start = input("Would you like to start? Y or N: ")
print(start)
if start.lower() == "y":
    begin = input("Would you like to open the door or walk down the trail? type Door or Trail ")
    if begin.lower() == "trail":
        pond = input("Would you like to take the boat or swim across the pond? Type Boat or Swim ")
        if pond.lower() == "boat":
            door = input("You come to three doors yellow, red, and a blue door. Type Yellow, Red or Blue ")
            if door.lower() == "yellow":
                print("You found the loots")
            elif door.lower() == "blue":
                print("Game over. Monster ate you.")
            else:
                print("Game over. Troll stabbed you.")

        else:
              print("Game over. Crocks ate you swimming across.")
    else:
        print("Game over. Knight stapped you opening door.")
else:
    print("Restart game")





    






