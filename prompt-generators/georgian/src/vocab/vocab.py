import random

from vocab.transient_verbs import translate_prompt_transient_verb
from vocab.phrases import translate_prompt_phrase
from vocab.nouns import translate_prompt_noun
from vocab.adjectives import translate_prompt_adjective

def generate_vocab_prompt():
    return translate_prompt_noun()
    # return random.choice([
    #     translate_prompt_transient_verb,
    #     translate_prompt_phrase,
    #     translate_prompt_noun,
    #     translate_prompt_adjective
    # ])()