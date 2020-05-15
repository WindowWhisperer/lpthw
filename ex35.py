# Branches and Functions
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Learn to type a number Dude!")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("Greedy Bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps you.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through the door now.")
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and rips you open.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I don't know what you mean.")

def monster_room():
    print("Here you se the great monster, Xolatlhu")
    print("The moster stars at you and you feel yourself going insane.")
    print("Do you flee for your life or eat your arm?")

    choice = input ("> ")

    if "flee" in choice:
        start()
    elif "arm" in choice:
        dead("Well, at least your last meal with tasty!")
    else:
        monster_room

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You're in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input ("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        monster_room()
    else:
        dead("You stumble around in the room until you fall asleep, perchance to dream.")


start()
