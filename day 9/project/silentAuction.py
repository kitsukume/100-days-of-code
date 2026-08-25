import art
auction = {}
exit = "y"
while exit == "y":
    print(art.gavel)
    print("Welcome to the silent auction \n")
    name = input("What is your name? \n").lower()
    bid = int(input("How much would you like to bid? \n$"))
    exit = input("Are there other bidders? Y or N \n").lower()
  
    auction[name] = bid
    print("\n" *100)
highest_bid = 0
highest_name = ""
for key in auction:
    
    if highest_bid < auction[key]:
        highest_bid = auction[key]
        highest_name = key

print(f"{highest_name.capitalize()} won with the highest bid of ${highest_bid}")