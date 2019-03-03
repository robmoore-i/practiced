#!/usr/bin/python3

import random

transient_verbs = ["help", "give", "eat", "drink", "buy", "add"]

def translate_prompt():
    return "Translate \"" + random.choice(transient_verbs) + "\""

print(translate_prompt())

exit(0)
