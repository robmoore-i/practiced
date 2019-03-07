from assertpy import assert_that
from tick import print_test_success
from transient_verbs import transient_verbs, translate_prompt_transient_verb_ge_en, translate_prompt_transient_verb_en_ge

print(__file__)

def invert_map(m):
    return {v: k for k, v in m.items()}

def assert_prompt_and_answer_are_consistent_for_en_ge(prompt):
    assert_that(prompt["prompt"]).contains(invert_map(transient_verbs)[prompt["answer"]])
    print_test_success("Prompt and answer are consistent for en -> ge")

def assert_prompt_and_answer_are_consistent_for_ge_en(prompt):
    assert_that(prompt["prompt"]).contains(transient_verbs[prompt["answer"]])
    print_test_success("Prompt and answer are consistent for ge -> en")

assert_prompt_and_answer_are_consistent_for_en_ge(translate_prompt_transient_verb_en_ge())
assert_prompt_and_answer_are_consistent_for_ge_en(translate_prompt_transient_verb_ge_en())