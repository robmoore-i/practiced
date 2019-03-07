import json
from assertpy import assert_that

from transient_verbs import transient_verbs
from generate_prompt import translate_prompt, prompt_text

def assert_prompt_has_correct_json_format(prompt):
    assert_that(sorted(list(prompt.keys()))).is_equal_to(["answer", "prompt"])

def invert_map(m):
    return {v: k for k, v in m.items()}

def assert_either(do_assertion_a, do_assertion_b):
    try:
        do_assertion_a()
    except:
        do_assertion_b()

def assert_prompt_and_answer_are_consistent(prompt):
    assert_either(
        lambda: assert_that(prompt["prompt"]).contains(transient_verbs[prompt["answer"]]),
        lambda: assert_that(prompt["prompt"]).contains(invert_map(transient_verbs)[prompt["answer"]])
    )

def assert_printed_output_is_valid_stringified_json(printed_output, prompt):
    assert_that(json.loads(printed_output)).is_equal_to(prompt)

def test_prompt(printed_output, prompt):
    assert_prompt_has_correct_json_format(prompt)
    assert_prompt_and_answer_are_consistent(prompt)
    assert_printed_output_is_valid_stringified_json(printed_output, prompt)

# Run tests

prompt = translate_prompt()
printed_output = prompt_text(prompt)

test_prompt(printed_output, prompt)