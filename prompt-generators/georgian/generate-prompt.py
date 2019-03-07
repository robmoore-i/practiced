#!/usr/local/bin/python3

##### Code #####

import random
from transient_verbs import transient_verb_generated_prompts, transient_verbs

def translate_prompt():
    potential_prompts = transient_verb_generated_prompts
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
