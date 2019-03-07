import screeve_form
from screeve_form import random_screeve
import noun
from person_marker import random_person
from verb import random_verb

def translate_prompt_en_ge(person, screeve, verb, noun):
    use_present_continuous = screeve == screeve_form.PRESENT_CONTINUOUS

    return {
        "prompt": "Translate \"" + person.en + " " + verb.conjugate_en(person, use_present_continuous) + " " + noun.en + "\"",
        "answer": verb.conjugate_ge(person) + " " + noun.accusative_ge()
    }

def translate_prompt_programming():
    return translate_prompt_en_ge(random_person(), random_screeve(), random_verb(), noun.CODE)

software_pidgin_prompt_generators = [
    translate_prompt_programming
]