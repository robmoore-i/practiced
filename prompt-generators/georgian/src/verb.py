import person_marker

class Verb:
    def __init__(self):
        pass
    
    def conjugate_en(self, person):
        if person == person_marker.I or person == person_marker.YOU or person == person_marker.WE or person == person_marker.YOUS:
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
        elif person == person_marker.WE:
            return "ვწერთ"
        else:
            return "წერთ"

WRITE = Verb()