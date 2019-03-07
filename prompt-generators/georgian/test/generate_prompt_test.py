import json
from assertpy import assert_that

from generate_prompt import generate_prompt, prompt_text

def assert_prompt_has_correct_json_format(prompt):
    assert_that(sorted(list(prompt.keys()))).is_equal_to(["answer", "prompt"])

def assert_prompt_values_have_correct_type(prompt):
    assert_that(prompt["prompt"]).is_type_of(str)
    assert_that(prompt["answer"]).is_type_of(str)

def assert_printed_output_is_valid_stringified_json(printed_output, prompt):
    assert_that(json.loads(printed_output)).is_equal_to(prompt)

def test_prompt(printed_output, prompt):
    assert_prompt_has_correct_json_format(prompt)
    assert_prompt_values_have_correct_type(prompt)
    assert_printed_output_is_valid_stringified_json(printed_output, prompt)

# Run tests

prompt = generate_prompt()
printed_output = prompt_text(prompt)

test_prompt(printed_output, prompt)

print(__file__ + " ✔️")