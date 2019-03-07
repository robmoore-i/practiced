import random
import person_marker

class Verb:
    def __init__(self, en_root, ge_neutral):
        self.en_root = en_root
        self.ge_neutral = ge_neutral
    
    def conjugate_en(self, person):
        if person == person_marker.SHE or person == person_marker.HE:
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

def random_verb():
    return random.choice([WRITE, BUILD])