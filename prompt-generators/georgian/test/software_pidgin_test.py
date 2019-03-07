from assertpy import assert_that

import person_marker
import screeve
import verb
import noun
from software_pidgin import translate_prompt_en_ge

def assert_translation_for_present_programming(verb, person, en, ge):
    prompt = translate_prompt_en_ge(person, screeve.PRESENT, verb, noun.CODE)
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
        assert_translation_for_present_programming(verb.WRITE, person, en, ge)

def assert_translations_for_present_building_of_code():
    inputs = [
        (person_marker.I, "I build code", "ვაშენებ კოდს"),
        (person_marker.YOU, "You build code", "აშენებ კოდს"),
        (person_marker.SHE, "She builds code", "აშენებს კოდს"),
        (person_marker.HE, "He builds code", "აშენებს კოდს"),
        (person_marker.WE, "We build code", "ვაშენებთ კოდს"),
        (person_marker.YOUS, "You build code", "აშენებთ კოდს"),
        (person_marker.THEY, "They build code", "აშენებენ კოდს")
    ]

    for (person, en, ge) in inputs:
        assert_translation_for_present_programming(verb.BUILD, person, en, ge)

assert_translations_for_present_writing_of_code()
assert_translations_for_present_building_of_code()

print(__file__ + " ✔️")