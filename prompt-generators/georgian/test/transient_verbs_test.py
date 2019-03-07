from assertpy import assert_that
from transient_verbs import transient_verbs, translate_prompt_transient_verb_ge_en, translate_prompt_transient_verb_en_ge

def invert_map(m):
    return {v: k for k, v in m.items()}

def assert_prompt_and_answer_are_consistent_for_en_ge(prompt):
    assert_that(prompt["prompt"]).contains(invert_map(transient_verbs)[prompt["answer"]])

def assert_prompt_and_answer_are_consistent_for_ge_en(prompt):
    assert_that(prompt["prompt"]).contains(transient_verbs[prompt["answer"]])

# Run tests

assert_prompt_and_answer_are_consistent_for_en_ge(translate_prompt_transient_verb_en_ge())
assert_prompt_and_answer_are_consistent_for_ge_en(translate_prompt_transient_verb_ge_en())

print(__file__ + " ✔️")