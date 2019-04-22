import json
from assertpy import assert_that

from tick import print_test_success
from generate_prompt import PromptGenerator

print(__file__)

test_prompt_generator = PromptGenerator(".")

fuzz_size = 1000

def generate_prompt():
    return test_prompt_generator.generate_prompt()

def assert_prompt_has_correct_json_format(prompt):
    assert_that(sorted(list(prompt.keys()))).is_equal_to(["answer", "prompt"])

def fuzz_assert_prompt_has_correct_json_format():
    for i in range(0, fuzz_size):
        prompt = generate_prompt()
        assert_prompt_has_correct_json_format(prompt)

    print_test_success("Prompt has keys 'answer' and 'prompt'")

def assert_prompt_values_have_correct_type(prompt):
    assert_that(prompt["prompt"]).is_type_of(str)
    assert_that(prompt["answer"]).is_type_of(str)

def fuzz_assert_prompt_values_have_correct_type():
    for i in range(0, fuzz_size):
        prompt = generate_prompt()
        assert_prompt_values_have_correct_type(prompt)

    print_test_success("Prompt fields are all strings")
    
def assert_printed_output_is_valid_stringified_json(prompt):
    assert_that(json.loads(json.dumps(prompt))).is_equal_to(prompt)
    
def fuzz_assert_printed_output_is_valid_stringified_json():
    for i in range(0, fuzz_size):
        prompt = generate_prompt()
        assert_printed_output_is_valid_stringified_json(prompt)

    print_test_success("Printed json output can be loaded into a python dictionary")

fuzz_assert_prompt_has_correct_json_format()
fuzz_assert_prompt_values_have_correct_type()
fuzz_assert_printed_output_is_valid_stringified_json()