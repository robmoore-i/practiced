import random

transient_verbs = {
    "help": "ეხმარებ",
    "eat": "ჭამ",
    "drink": "სვამ",
    "buy": "ყიდულობ",
    "add": "ამატებ",
    "build": "აშენებ",
    "work": "მუშაობ",
    "write": "წერ",
    "see": "ხედავ"
}

def random_verb():
    return random.choice(list(transient_verbs.keys()))

def translate_prompt_transient_verb_ge_en():
    verb = random_verb()
    return {
        "prompt": "What is the english for \"" + transient_verbs[verb] + "\"?",
        "answer": verb
    }

def translate_prompt_transient_verb_en_ge():
    verb = random_verb()
    return {
        "prompt": "What is the georgian neutral form for \"" + verb + "\"?",
        "answer": transient_verbs[verb]
    }

transient_verb_generated_prompts = [
    translate_prompt_transient_verb_ge_en(),
    translate_prompt_transient_verb_en_ge()
]