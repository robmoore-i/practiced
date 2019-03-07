import person_marker

class Verb:
    def __init__(self):
        pass
    
    def conjugate_en(self, person):
        if person == person_marker.I or person == person_marker.YOU or person == person_marker.WE:
            return "write"
        else:
            return "writes"
    
    def conjugate_ge(self, person):
        if person == person_marker.I:
            return "ვწერ"
        elif person == person_marker.YOU:
            return "წერ"
        elif person == person_marker.SHE or person == person_marker.HE:
            return "წერს"
        else:
            return "ვწერთ"

WRITE = Verb()