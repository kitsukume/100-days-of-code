def calculate_love_score(name1, name2):
    t_count = 0
    l_count = 0
    name = name1 + name2
    for letter in name:
        if letter in "true":
            t_count += 1
        if letter in "love":
            l_count += 1

    count = str(t_count) + str(l_count)
    print(f"Your love score is: {count}")



calculate_love_score("Someone", "Someone else")