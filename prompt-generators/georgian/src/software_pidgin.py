import screeve
import noun
from person_marker import random_person
from verb import random_verb

def translate_prompt_en_ge(person, screeve, verb, noun):
    return {
        "prompt": "Translate \"" + person.en + " " + verb.conjugate_en(person) + " code\"",
        "answer": verb.conjugate_ge(person) + " კოდს"
    }

def translate_prompt_programming():
    return translate_prompt_en_ge(random_person(), screeve.PRESENT, random_verb(), noun.CODE)

software_pidgin_prompt_generators = [
    translate_prompt_programming
]