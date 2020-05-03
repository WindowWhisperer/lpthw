people = 30
cars = 40
trucks = 15

if cars > people:
    print("Take cars.")
elif cars < people:
    print("Don't take cars.")
else:
    print("Not sure.")

if trucks > cars:
    print("Too many trucks. Not good for climate.")
elif trucks < cars:
    print("Could take trucks.")
else:
    print("Still not sure.")

if people > trucks:
    print("Let's just take the trucks - oh wait, we're under quarantine")
else:
    print("Fine, let's stay home then.")
