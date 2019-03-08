from assertpy import assert_that

from tick import print_test_success
import person_marker
import screeve_form
import verb
import noun
from software_pidgin import translate_prompt_en_ge

print(__file__)

# Pre: n > len(s)
def pad(s, n):
    return s + (" " * (n - len(s)))

def with_padding(s):
    return pad(s, 10)

def wrap_sentence_part(s):
    return "[" + s + "]"

def translation_test_description_part(s):
    return with_padding(wrap_sentence_part(s))

def print_translation_test_description(person_en, verb_en_root, noun_en):
    person_part = translation_test_description_part(person_en)
    verb_part = translation_test_description_part(verb_en_root)
    noun_part = translation_test_description_part(noun_en)
    print_test_success(person_part + verb_part + noun_part)

def assert_translation_for_present_programming(verb, person, en, ge):
    prompt = translate_prompt_en_ge(person, screeve_form.PRESENT, verb, noun.CODE)
    assert_that(prompt["prompt"]).is_equal_to("Translate \"" + en + "\"")
    assert_that(prompt["answer"]).is_equal_to(ge)
    print_translation_test_description(person.en, verb.en_root, noun.CODE.en)

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

def assert_translation_for_present_continuous_reading(person, noun, en, ge):
    prompt = translate_prompt_en_ge(person, screeve_form.PRESENT_CONTINUOUS, verb.READ, noun)
    assert_that(prompt["prompt"]).is_equal_to("Translate \"" + en + "\"")
    assert_that(prompt["answer"]).is_equal_to(ge)
    print_translation_test_description(person.en, verb.READ.en_root, noun.en)

def assert_translations_for_present_reading_a_book():
    inputs = [
        (person_marker.I, "I am reading a book", "ვკითხულობ წიგნს"),
        (person_marker.YOU, "You are reading a book", "კითხულობ წიგნს"),
        (person_marker.SHE, "She is reading a book", "კითხულობს წიგნს"),
        (person_marker.HE, "He is reading a book", "კითხულობს წიგნს"),
        (person_marker.WE, "We are reading a book", "ვკითხულობთ წიგნს"),
        (person_marker.YOUS, "You are reading a book", "კითხულობთ წიგნს"),
        (person_marker.THEY, "They are reading a book", "კითხულობენ წიგნს")
    ]

    for (person, en, ge) in inputs:
        assert_translation_for_present_continuous_reading(person, noun.BOOK, en, ge)

assert_translations_for_present_writing_of_code()
assert_translations_for_present_building_of_code()
assert_translations_for_present_reading_a_book()