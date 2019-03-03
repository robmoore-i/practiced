#!/usr/bin/python3

import random

transient_verbs = {
    "help": "ეხმარებ",
    "eat": "ჭან",
    "drink": "სვამ",
    "buy": "ყიდულობ",
    "add": "ამატებ",
    "build": "აშენებ",
    "work": "მუშაობ",
    "write": "დაწერა"
}

def translate_prompt():
    return "What is the neutral form of \"" + random.choice(list(transient_verbs.keys())) + "\"?"

print(translate_prompt())

exit(0)
