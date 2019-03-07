import random

class Person:
    def __init__(self, en):
        self.en = en

I = Person("I")
YOU = Person("You")
SHE = Person("She")
HE = Person("He")
WE = Person("We")
YOUS = Person("You")
THEY = Person("They")

def random_person():
    return random.choice([I, YOU, SHE, HE, WE, YOUS, THEY])