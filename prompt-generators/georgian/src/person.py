class Number:
    def __init__(self, description):
        self.description = description

SINGULAR = Number("one")
PLURAL = Number("multiple")

class Person:
    def __init__(self, en, number):
        self.en = en

I = Person("I", SINGULAR)
YOU = Person("You", SINGULAR)
SHE = Person("She", SINGULAR)