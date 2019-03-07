import person as person_markers

def translate_prompt_en_ge(person, screeve, verb, noun):
    if person == person_markers.I:
        person_en = "I"
        verb_ge = "ვწერ"
        verb_en = "write"
    elif person == person_markers.YOU:
        person_en = "You"
        verb_ge = "წერ"
        verb_en = "write"
    else:
        person_en = "She"
        verb_ge = "წერს"
        verb_en = "writes"

    return {
        "prompt": "Translate \"" + person_en + " " + verb_en + " code\"",
        "answer": verb_ge + " კოდი"
    }