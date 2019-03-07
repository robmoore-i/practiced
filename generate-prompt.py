#!/usr/local/bin/python3

import random

transient_verbs = {
    "help": "ეხმარებ",
    "eat": "ჭან",
    "drink": "სვამ",
    "buy": "ყიდულობ",
    "add": "ამატებ",
    "build": "აშენებ",
    "work": "მუშაობ",
    "write": "წერ",
    "see": "ხედავ"
}

def translate_english_to_georgian():
    return "What is the neutral form of \"" + random.choice(list(transient_verbs.keys())) + "\"?"

def translate_georgian_to_english():
    return "What english verb is \"" + random.choice(list(transient_verbs.keys())) + "\" the neutral form of?"

def translate_prompt():
    return translate_english_to_georgian()

print(translate_prompt())

exit(0)
