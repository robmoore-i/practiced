import random

import grammar.person_marker as person_marker
import grammar.screeve_form as screeve_form

class Verb:
    def __init__(self, en_root, ge_neutral):
        self.en_root = en_root
        self.ge_neutral = ge_neutral
    
    def conjugate_en(self, person, screeve):
        if screeve == screeve_form.PRESENT_CONTINUOUS:
            return conjugate_to_be_en(person) + " " + drop_trailing_e(self.en_root) + "ing"
        elif person == person_marker.SHE or person == person_marker.HE:
            return self.en_root + "s"
        else:
            return self.en_root
    
    def conjugate_ge(self, person):
        if person == person_marker.I:
            return "ვ" + self.ge_neutral
        elif person == person_marker.YOU:
            return self.ge_neutral
        elif person == person_marker.SHE or person == person_marker.HE:
            return self.ge_neutral + "ს"
        elif person == person_marker.WE:
            return "ვ" + self.ge_neutral + "თ"
        elif person == person_marker.YOUS:
            return self.ge_neutral + "თ"
        else:
            return self.ge_neutral + "ენ"

WRITE = Verb("write", "წერ")
BUILD = Verb("build", "აშენებ")
READ = Verb("read", "კითხულობ")

def random_verb():
    return random.choice([WRITE, BUILD, READ])

def conjugate_to_be_en(person):
    if person == person_marker.I:
        return "am"
    elif person == person_marker.YOU or person == person_marker.WE or person == person_marker.YOUS or person == person_marker.THEY:
        return "are"
    else:
        return "is"

def drop_trailing_e(s):
    if (s[-1] == "e"):
        return s[:-1]
    else:
        return s