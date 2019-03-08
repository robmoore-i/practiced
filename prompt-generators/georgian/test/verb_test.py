from assertpy import assert_that

from tick import print_test_success
import verb
import person_marker
import screeve_form

print(__file__)

def assert_drops_trailing_vowel_for_present_continuous_verbs():
    assert_that(verb.WRITE.conjugate_en(person_marker.I, screeve_form.PRESENT_CONTINUOUS)).is_equal_to("am writing")
    print_test_success("Drops trailing vowel for present continuous verbs")

assert_drops_trailing_vowel_for_present_continuous_verbs()