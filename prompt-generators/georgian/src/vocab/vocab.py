import random

from vocab.transient_verbs import translate_prompt_transient_verb
from vocab.consultant_phrases import translate_prompt_consultant_phrase

def generate_vocab_prompt():
    return random.choice([
        translate_prompt_transient_verb,
        translate_prompt_consultant_phrase
    ])()