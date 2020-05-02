def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply (a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide (a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print ("Let's do math with just functions!")

age = add (30, 7)
height = subtract (70, 1)
weight = multiply (110, 2)
iq = divide ( 270, 2)

print(f"Age {age}, height in inches {height}, weight in pounds or kilos? {weight}, and IQ {iq}")

what = add (age, multiply (weight, height))

print ("That becomes: ", what)