#Making Decisions

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2? 
Type the number of the door you choose.""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do? Enter the number of your choice.")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    print("3. Run away")

    bear = input("> ")

    if bear == "1":
        print("""You take one delicious bite. I hope it was worth it because the
        bear rips off your face.""")
    elif bear == "2":
        print("The bear laughs at you and then turns you into a cake topper.")
    elif bear == "3":
        print("You're safe to live another day.")
    else:
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss of a monster's retina. It says, \"feed me\", and you look for what you can feed it.")
    print("You see \n1. blueberries, 2. yellow clothespins, and 3. red jello. What do you choose?")

    monster_food = input("> ")

    if monster_food == "1" or monster_food == "2":
        print("The monster eats the food you have offered and burps in satisfaction. You are safe!")

    elif monster_food == "3":
        print("The monster eats the jello and goes into anaphylaxis. You are safe.")

    else:
        print("The monster suddenly explodes and you are covered in goo. Good job!")

else:
    print("You stumble around in the dark before falling to sleep. You will smell in the morning. ")