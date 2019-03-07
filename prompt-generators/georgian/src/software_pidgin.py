import person as person_markers

def translate_prompt_en_ge(person, screeve, verb, noun):
    if person == person_markers.I:
        verb_ge = "ვწერ"
        verb_en = "write"
    elif person == person_markers.YOU:
        verb_ge = "წერ"
        verb_en = "write"
    else:
        verb_ge = "წერს"
        verb_en = "writes"

    return {
        "prompt": "Translate \"" + person.en + " " + verb_en + " code\"",
        "answer": verb_ge + " კოდი"
    }