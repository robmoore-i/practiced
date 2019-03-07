import person_marker

class Verb:
    def __init__(self):
        pass
    
    def conjugate_en(self, person):
        if person == person_marker.I:
            return "write"
        elif person == person_marker.YOU:
            return "write"
        else:
            return "writes"
    
    def conjugate_ge(self, person):
        if person == person_marker.I:
            return "ვწერ"
        elif person == person_marker.YOU:
            return "წერ"
        else:
            return "წერს"

WRITE = Verb()