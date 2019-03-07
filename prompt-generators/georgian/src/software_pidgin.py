def translate_prompt_en_ge(person, screeve, verb, noun):
    return {
        "prompt": "Translate \"" + person.en + " " + verb.conjugate_en(person) + " code\"",
        "answer": verb.conjugate_ge(person) + " კოდს"
    }