import json
from assertpy import assert_that

from tick import print_test_success
from generate_prompt import generate_prompt, prompt_text

print(__file__)

def assert_prompt_has_correct_json_format(prompt):
    assert_that(sorted(list(prompt.keys()))).is_equal_to(["answer", "prompt"])

def fuzz_assert_prompt_has_correct_json_format():
    for i in range(0, 50):
        prompt = generate_prompt()
        assert_prompt_has_correct_json_format(prompt)

    print_test_success("Prompt has keys 'answer' and 'prompt'")

def assert_prompt_values_have_correct_type(prompt):
    assert_that(prompt["prompt"]).is_type_of(str)
    assert_that(prompt["answer"]).is_type_of(str)

def fuzz_assert_prompt_values_have_correct_type():
    for i in range(0, 50):
        prompt = generate_prompt()
        assert_prompt_values_have_correct_type(prompt)

    print_test_success("Prompt fields are all strings")
    
def assert_printed_output_is_valid_stringified_json(printed_output, prompt):
    assert_that(json.loads(printed_output)).is_equal_to(prompt)
    
def fuzz_assert_printed_output_is_valid_stringified_json():
    for i in range(0, 50):
        prompt = generate_prompt()
        printed_output = prompt_text(prompt)
        assert_printed_output_is_valid_stringified_json(printed_output, prompt)
    
    print_test_success("Printed json output can be loaded into a python dictionary")

fuzz_assert_prompt_has_correct_json_format()
fuzz_assert_prompt_values_have_correct_type()
fuzz_assert_printed_output_is_valid_stringified_json()