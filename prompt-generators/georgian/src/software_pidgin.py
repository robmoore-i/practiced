import person as person_markers

def translate_prompt_en_ge(person, screeve, verb, noun):
    if person == person_markers.I:
        person_en = "I"
        verb_ge = "ვწერ"
    else:
        person_en = "You"
        verb_ge = "წერ"

    return {
        "prompt": "Translate \"" + person_en + " write code\"",
        "answer": verb_ge + " კოდი"
    }