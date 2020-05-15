class Song(object):
    def __init__(self, lyrics): # note double underscore on both sides
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_birthday = Song(["Happy birthday to you",
                       "I don't want to get sued",
                       "So I'll stop right there"])

lambs_parade = Song(["They rally around the family,",
                        "With pockets full of wool."])

happy_birthday.sing_me_a_song()

lambs_parade.sing_me_a_song()

