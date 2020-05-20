from sys import exit
from random import randint
import random
from textwrap import dedent
import linecache

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

class Scene(object):
    def enter(self): 
         exit(1)

class KingsCourt(Scene):
    def enter(self):
        print("what is your name?")

        player_name = input('> ')

        print(dedent(f"""
       {player_name},you are standing in the throne room of King Goodwin of Gallafrey, Lord Majesty of the Seven Dales.
        You have just asked him for permission to marry his daughter, Princess Gaia. 
        He stares at you for a few moments that feel like hours as he measures your request. Then, he says:
        \"The one who marries my daughter must be smart, brave, and just. You must prove yourself by completing two challenges - dealing with a monster and finding a precious item.
        Are you ready? yes or no\"
        """))
        answer = input("> ")

        if answer == "yes" or "y":
            return random.choice(['cave', 'mountain'])
        
        elif answer == "no" or "n":
            print("A better one than you would have accepted the challenge. Your future with the princess does not look bright")
            exit(1)

        else: 
            print("That wasn't one of the choices offered. You failed to live up to the king's standards.")
            return 'death'

class Cave(Scene):
    
    lang_troll = linecache.getline('lpthw/languages.txt', 12)
    song_troll = linecache.getline('lpthw/new_file.txt', 2)

    def enter(self):
        print(dedent("""
            You're walking along a path deep in the forest that takes you near the entrance of an old cave. You smell moist rock, stale air, and the combination of tobacco and elderflower that signifies a troll is near.
            You need to get the princess' gold necklace back from the troll who bought it from a guy who bought it from the theif who took it during the Festival of the 3rd Dale. When originally accused, the troll lawyered up,
            so the princess will have to wait for court proceedings to get the necklace back unless you can prevail.
            You could sneak into the cave, stage a distraction, or attack the troll? What do you do?
             """))
        
        response = input("> ")

        if response == "sneak" or "cave" or "stage" or "distract" or "distraction":
            print(dedent("""
                The troll's attention elsewhere, you slip passed him into the shadows. You see clearly why trolls have a reputation for being messy.
                This troll has stuff everywhere and there doesn't seem to be any rhyme or reason for the placement. Half eaten banana peels are next to paper and ink,
                the sofa is covered with dried rice, fresh flowers, and ancient manuscripts, and all the shelves are filled with shoes, games, and collector's edition salt and pepper shakers in no particular order.
                This necklace could be anywhere. You're going to have to come up with another plan, but before you can think of something,
                the troll finds you.
                \"How dare you break into my house!\" the troll screeches!
                You tell the troll you need the necklace that rightfully belongs to the princess.
                The troll says, \"That is not nearly a good enough reason for me to just give you what you want.
                I paid good money for this necklace and it is only a replica of the princess' necklace because I admire her so.
                But, I tell you what, I will play a game with you for it.\"...You could have guessed that it would come to this.
                All trolls have a passion for games, particularly if a wager can be made on the game...\"
                if you can tell me which cup has the pebble under it, I will give you the necklace. If not,
                then you must give me your shoes to add to my collection.\" 
                You stare as the troll flips 3 red plastic cups upside down onto the coffee table, then places a small pebble
                underneath the middle one. He sings a little tune \"{song_troll}\" in his native language, {lang_troll},
                while he rotates to mix the cups. He lines the cups along the edge of the table and tells you to 
                pick the number of the cup, 1-3, containing the rock.
                """))

            code = f"{randint(1,3)}"
            guess = input("[keypad]> ") 
            guesses = 0

            while guess != code and guesses < 3:
                print("No pebble!")
                guesses += 1
                guess = input("[keypad]> ")

            if guess == code:
                print(dedent("""
                    The troll shreeks when he sees the pebble under the cup you have choosen and slaps all the cups off the table.
                    You laugh and claim your prize. 
                    """))
                return 'mountain'

            else:
                print(dedent("""
                    You lose! You walk away empty handed and empty footed, as the troll places your shoes near an empty container of Ramen
                    noodles on his shelf. Maybe you can find a replica, but you'll definitely need a new monster challenge.
                    """))
                return 'mountain'

        else:
            print("All you succeed in doing is making the troll angry. It strangles you with the necklace.") 
            return 'death'
    
class Mountain(Scene):

    
    def enter(self):
        
        print(dedent("""
        You're climbing to the top of Mt. Greyborn, where Silverous the Dragon lives, to stop this monster from terrorizing the town. 
        All is quiet as you approach the summit, but you see a flash of silvery scales, so you know the dragon is home.
        You could take advantage of the surprise factor and launch a sneak attack, or you could take advantage of the dragon's greed to make a deal with him.
        What do you choose? attack or deal
        """))
        
        action = input("> ")

        if action == "attack":
            print(dedent("""
                You tiptoe toward the dragon until you are in striking range. You grab your diamond dagger from your belt, leap into the air, and plung the dagger deep into he dragon's brain.
                The dragon starts to scream, but is dead before his mouth gets a chance to open. The town is safe from this dragon.
                """))
            return random.choice(['forest', 'island'])
        
        elif action == "deal":
            lang = linecache.getline('languages.txt', 10)
            print(f"You utter the one safe word you know in the Dragon language, \"{lang}\"")
            print("""
                The dragon growls a little as he lifts himself up and turns around to look at you. His breath is hot 
                on your face. But, you aren't dead, so you keep talking.
                \"Might Silverous\" -- dragons love flattery --\"I have come all this way to see you because I have something
                to offer you.\"
                Silverous shows his fangs and you flinch, but it turns out that he is smiling.
                \"Your life, traveler?\"
                \"Ah...erm...well, no...but I have something you will like even better.\"
                 You pull the gleaming gold necklace from you bag. On seeing this, the dragon's eyes narrow, as if the only thing he can see is the gold. He starts to salivate
                \"I will give you this necklace if you promise never again to terrorize anywhere in the Seven Dales\"
                \"Traveler,\" the dragon booms, \"What is to keep me from taking the necklace and continuing to terroize the town?\"
                \"This is the Princess' necklace and she will bestow it as a sign of respect for all of the lands to see.
                She will issue a decree that you are now a beloved dragon who has great favor with the Royal Family. No one will hurt you
                and you will be invited to take a starring role in the parade each year and you can even help us defend the Seven Dales from any invaders.
                You will be a hero and a legend as long as the Kingdom prevails.\" -- all dragons really want is respect...and gold.
                Silverous' eyes well up with tears. \"She would do that for me, traveller?\"
                \"She has given me her word.\"
                Silverous takes the necklace and says, \"It's a deal!\"
                Now you just have to complete the last challenge!
                Will you retrieve a rare black pearl or a hair from a unicorn's tail? Choose now, pearl or unicorn:
                """)

            select = input("> ")

            if select == "pearl":
                return 'island'

            elif select == "unicorn":
                return 'forest'
            
            else: 
                print("You took too long. The dragon heard you and burned you like a brisket.")
                return 'death'
        

class Forest(Scene):
     def enter(self):
        
        print(dedent("""Your last challenge is to return with a hair from a unicorn's tail. Folklore says unicorns live deep in the
        Friendship Forest, so that's where you go. Unicorns are supposedly very friendly, but if they are surprised, they can attack.
        As the forest grows darker, you see a flash or rainbow and sparkles. You slowly approach. Yes! You have found a unicorn.
        What will you do next? Ask for its help, pluck a hair and run, or offer it a treat?
        """))
    
        answer = input("> ")

        if answer == "pluck" or "pluck a hair" or "attack" or "kill":
            print("You've startled it and the magical creature stabs you with its horn.")
            return 'death'

        else: 
            print("That worked! The unicorn becomes your friend and is happy to help! The unicorn will definitely get a wedding invite from you.")
            return 'finished'
    
class Island(Scene):
        def enter(self):
            print(dedent("""
                Your last challenge is to retrive a rare black pearl. You find a boat captain to take you out
                to a small island where the oysters are most likely to provide a black pearl. You find 9 possible oysters
                but the law limits your taking only 8 per trip without a license. Which one will you pick?
                """))
        
            code = f"{randint(1,9)}"
            guess = input("[number]> ") 
            guesses = 0

            while guess != code and guesses < 7:
                print("You crack open the oyster shell. No pearl")
                guesses += 1
                guess = input("[keypad]> ")
        
            if guess == code:
                print(dedent("""
                    The shell opens and there is a beautiful black pearl! You thank the oyster and hurry to show the King.") 
                    """))
                return 'finished'
            else:
                print("A pearl! But this on is white. You'll have to find another precious item to retrieve.")
                return 'forest'

class Death(Scene):

    quips = [
        "Your death certificate says you died of dysentery",
        "Maybe in your next life, you'll get this right. Game over.",
        "No one will find your body for a 100 years."
        ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        print("Would you like to play again?")
        
        answer = input('[Y/N]> ')
        if answer == "yes" or "y" or "Yes" or "Yes":
            return 'kings_court'
        else:
            exit(1)

class Finished(Scene):
    def enter(self):
        print("You have completed the King's Challenges. The princess happily agrees to marry someone so smart, brave, and just. The date is set and wedding bells await! Congratulations!")
        print("Would you like to play again?")
        
        answer = input('> ')
        if answer == "yes" or "y" or "ok" or "sure" or "Yes" or "Y":
            return 'kings_court'
        else:
            return exit(1) #or could be finished


class Map (object):
    scenes = {
        'kings_court': KingsCourt(),
        'cave': Cave(),
        'mountain': Mountain(),
        'forest': Forest(),
        'island': Island(),
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

    
a_map = Map('kings_court')
a_game = Engine(a_map)
a_game.play()


