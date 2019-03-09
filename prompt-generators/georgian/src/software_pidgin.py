import random
import noun
import verb
from screeve_form import random_screeve
from person_marker import random_person

def translate_prompt_en_ge(person, screeve, verb, noun):
    return {
        "prompt": "Translate \"" + person.en + " " + verb.conjugate_en(person, screeve) + " " + noun.en + "\"",
        "answer": verb.conjugate_ge(person) + " " + noun.accusative_ge()
    }

# anyone | read, write, build | code
def translate_prompt_code():
    return translate_prompt_en_ge(random_person(), random_screeve(), verb.random_verb(), noun.CODE)

# anyone | read | book
def translate_prompt_read_book():
    return translate_prompt_en_ge(random_person(), random_screeve(), verb.READ, noun.BOOK)

def translate_prompt_consultant_phrase():
    phrases = {
        "It depends": "გააჩნია",
        "What does it cost?": "რა ღირს",
        "I don't know": "არ ვიცი",
        "I don't understand": "არ მესმის",
        "I agree with you": "გეთანხმებით",
        "I think so": "ასე ვფიქრობ",
        "I like it": "მომწონს",
        "Please don't": "არა რა",
        "I prefer it": "მირჩევნია"
    }

    random_index = random.choice([i for i in range(0, len(phrases))])
    (en, ge) = list(phrases.items())[random_index]
    return {
        "prompt": "როგორაა ქართულად \"" + en + "\"?",
        "answer": ge
    }

def translate_prompt_software():
    return random.choice([translate_prompt_code, translate_prompt_read_book, translate_prompt_consultant_phrase])()