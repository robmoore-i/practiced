from assertpy import assert_that

import person_marker
import screeve
import verb
import noun
from software_pidgin import translate_prompt_en_ge

def assert_translation_for_present_writing_of_code(person, en, ge):
    prompt = translate_prompt_en_ge(person, screeve.PRESENT, verb.WRITE, noun.CODE)
    assert_that(prompt["prompt"]).is_equal_to("Translate \"" + en + "\"")
    assert_that(prompt["answer"]).is_equal_to(ge)

def assert_generates_I_write_code():
    assert_translation_for_present_writing_of_code(person_marker.I, "I write code", "ვწერ კოდი")

def assert_generates_you_write_code():
    assert_translation_for_present_writing_of_code(person_marker.YOU, "You write code", "წერ კოდი")
    
def assert_generates_she_writes_code():
    assert_translation_for_present_writing_of_code(person_marker.SHE, "She writes code", "წერს კოდი")

def assert_generates_he_writes_code():
    assert_translation_for_present_writing_of_code(person_marker.HE, "He writes code", "წერს კოდი")
    
assert_generates_I_write_code()
assert_generates_you_write_code()
assert_generates_she_writes_code()
assert_generates_he_writes_code()

print(__file__ + " ✔️")