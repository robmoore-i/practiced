import person as person_markers

def translate_prompt_en_ge(person, screeve, verb, noun):
    if person == person_markers.I:
        verb_ge = "ვწერ"
    elif person == person_markers.YOU:
        verb_ge = "წერ"
    else:
        verb_ge = "წერს"

    return {
        "prompt": "Translate \"" + person.en + " " + verb.conjugate_en(person) + " code\"",
        "answer": verb_ge + " კოდი"
    }