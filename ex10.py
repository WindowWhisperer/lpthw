#Escape sequences
#"I am 5'9\" tall" escapes double-quote inside string
#"I am 5\'9" tall" escapes single-quote inside string
#\t horitzontal tab, \uXXXX character with 16 bit hex valuexxx 

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
black_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(black_cat)
print(fat_cat)