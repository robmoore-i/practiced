from assertpy import assert_that

import person
import screeve
import verb
import noun
from software_pidgin import translate_prompt_en_ge

def assert_generates_can_write_code():
    prompt = translate_prompt_en_ge(person.I, screeve.PRESENT, verb.WRITE, noun.CODE)
    assert_that(prompt["prompt"]).is_equal_to("Translate \"I write code\"")
    assert_that(prompt["answer"]).is_equal_to("ვწერ კოდი")

assert_generates_can_write_code()

print(__file__ + " ✔️")