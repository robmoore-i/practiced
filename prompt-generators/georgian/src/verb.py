import person as person_markers

class Verb:
    def __init__(self):
        pass
    
    def conjugate_en(self, person):
        if person == person_markers.I:
            return "write"
        elif person == person_markers.YOU:
            return "write"
        else:
            return "writes"
    
    def conjugate_ge(self, person):
        if person == person_markers.I:
            return "ვწერ"
        elif person == person_markers.YOU:
            return "წერ"
        else:
            return "წერს"

WRITE = Verb()