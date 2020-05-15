# Basic Object-Oriented Analysis and Design
# 1. Write about prob, 2. extract key concepts and research them, 3. create class hierarchy and object map, 4 code
#  the classes and test to run, 4. repeat/refine


from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        current_scene.enter()

class Death(Scene):

    quips = [
        "You've died of dysentery",
        "Maybe in your next life, you'll get this right. Game over.",
        "Not trying to be mean but...you dead."
        ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            The members of an advanced civilization, The Culture, have boarded your ship.
            You knew they were coming. They told you down to the second that they would board
            and that they would not harm you if you did not resist.
            You're running down the central corridor of the ship to the escape module to
            help the last of the crew board the escape module when a member of the Culture
            apparates in front of you blocking your way. Your options - shoot, negotiate, or run.
            """))

        action = input("> ")

        if action == "shoot":
            print(dedent("""
                Feeling a little trigger happy, you draw your blaster from the holster on your hip and fire it at the Culture Warrior.
                The Culture Warrior grabs his leg, falls to the floor, and is immediately replaced by
                an exact replica who kicks your blaster out of your hand and says \"You could have chosen peace. Now peace will choose you. Rest in peace.\"
                The new Culture Warrior transports you outside of the protection of the ship and your current life ends.
                """))
            return 'death'

        elif action == "run":
            print(dedent("""
                You stop on a dime and take off in the other direction, making The Flash look slow. 
                In your haste you bump your head on a low hanging part of the ceiling. When you awaken
                A Culture Warrior stands over you and says \"Fear not! We are here to help you and your primitive earthly
                civilization. Embrace the change. Embrace the Culture.\" 
                The Culture Warrior reaches towards you, open-handed, you duck and roll through a nearby door.
                """))
            return 'laser_weapon_armory'

        elif action == "negotiate":
            print(dedent("""
                You smile at the Culture Warrior, trying your best to look firm but friendly and say
                \"I take you at your word that you are here in peace. Let me get the rest of my crew to safety and we can speak together.\"
                The Warrior nods and permits this.
                The Culture Warrior says \"Your civilization is filled with hate and anger. For generations you have heard each other but now that you are
                traveling in space you pose a threat to other civilizations that we are sworn to protect. You must not go passed the Astroid belt until
                your world has eradicated poverty.\"
                \"There is a lot of good in the world too\" you say.
                \"A wonderful big bowl of soup can be spoiled by the presence of a maggot\" says the Warrior.
                \"You have a point there\" you say.
                \"You must agree to our terms - first fix yourself, then look elsewhere for adventure\" says the Warrior.
                \"The same could be said of the Culture, unless you testify that it is perfect\" you say.
                \"I don't have the power to do that\" the Warrior says.
                \"Then take me to your leader.\" you say.
                """))
            return 'escape_pod'

        else:
            print("That wasn't one of the options")
            return "the_bridge"

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You're in the Weapons Armory. You shut and lock the door you just rolled through to keep the Culture Warrior
            out. You scan the room for more Warriors that might be hiding. It's dead quiet. Too quiet. You run to the far side of the room
            and finding a bomb in its container.
            There's a keypad lock on the box and you need the code to get the bomb out. If you get the code
            wrong five times in a row, the lock seals forever. The code is 1 digit. 
            """))

        code = f"{randint(1,9)}"
        guess = input("[keypad]> ") 
        guesses = 0

        while guess != code and guesses < 5:
            print("BZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                The container clicks open and the seal breaks. You grab the bomb as fast as you can to the bridge where you must place it in the right spot. 
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                The lock buzzes one last time and then you hear a sickening melting sound as the mechanism is fuse together. The bomb explodes.
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You race to the Bridge and interrupt 3 Culture Warriors who are trying to take control of the ship to fly it back to their headquarters.
            They see you are holding a bomb stop what they are doing, mouths agape.
            You have three choices - detonate the bomb, tell a joke, call the president
            """))

        action = input("> ")
            
        if action == "detonate the bomb":
            print(dedent("""
                 With your crew safely away on the escape pod, you sacrifice your ship and life to stop the Culture Warriors. Will it truly stop them or does it just delay the inevitable. Only time will tell, but your time is up.
                """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                You decide laughter may be the best medicine for this situation and hope the Culture Warriors have a sense of humor. You say:
                \n\"DId you guys here that the galaxy's tongue twister champion just got arrested? I heard there going to give him a really tough sentence.\"
                You wait for a moment while the look of confusion on the Warriors' faces turns into smiles and then big belly laughter. Some are laughing so hard that they start to cry.
                The shortest one slaps you in a friendly way on the shoulder and says \n\"That's a good one. Why don't you come to meet our leader and tell him some more jokes?\"
                """))
            return 'escape_pod'

        elif action == "call the president":
            print(dedent("""
                You decide this ordeal is way above your pay grade so you call the president on her super secret phone number. She picks up on the first ring, saying \"Hello, Darling.\"
                """))
            return 'escape_pod'

class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You're on an escape pod traveling at half the speed of light towards the leader. As you stare out the window, you see your ship bursting into flames.
            You see the Culture Warrior next to you smile. He says \" you made a good choice.\"
            """))
        return 'finished'

class Finished(Scene):
        
    def enter(self):
        print("The leader is in good humor thanks to your awesome joke-telling and a peaceful truce is reached between the civilizations. You win. Everyone wins!")
        return 'finished'
        
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()