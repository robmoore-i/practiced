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

def assert_translations_for_present_writing_of_code():
    inputs = [
        (person_marker.I, "I write code", "ვწერ კოდს"),
        (person_marker.YOU, "You write code", "წერ კოდს"),
        (person_marker.SHE, "She writes code", "წერს კოდს"),
        (person_marker.HE, "He writes code", "წერს კოდს"),
        (person_marker.WE, "We write code", "ვწერთ კოდს"),
        (person_marker.YOUS, "You write code", "წერთ კოდს"),
        (person_marker.THEY, "They write code", "წერენ კოდს")
    ]

    for (person, en, ge) in inputs:
        assert_translation_for_present_writing_of_code(person, en, ge)

assert_translations_for_present_writing_of_code()

print(__file__ + " ✔️")