#!/usr/local/bin/python3

##### Code #####

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

def translate_prompt():
    potential_prompts = [
        translate_prompt_transient_verb_ge_en(),
        translate_prompt_transient_verb_en_ge()
    ]
    return random.choice(potential_prompts)

prompt = translate_prompt()
printed_output = str(prompt).replace("\"", "\\\"").replace("'", "\"")

##### Tests #####

import json
from assertpy import assert_that

# Check prompt format
assert_that(sorted(list(prompt.keys()))).is_equal_to(["answer", "prompt"])

# Check consistency between prompt and answer
def invert_map(m):
    return {v: k for k, v in m.items()}

def assert_either(do_assertion_a, do_assertion_b):
    try:
        do_assertion_a()
    except:
        do_assertion_b()

assert_either(
    lambda: assert_that(prompt["prompt"]).contains(transient_verbs[prompt["answer"]]),
    lambda: assert_that(prompt["prompt"]).contains(invert_map(transient_verbs)[prompt["answer"]])
)

# Check printed version can be read immediately into json
assert_that(json.loads(printed_output)).is_equal_to(prompt)

##### Execute #####

print(printed_output)
exit(0)
