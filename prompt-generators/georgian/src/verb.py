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

WRITE = Verb()