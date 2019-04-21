import random
from vocab.vocab_prompter import VocabPrompter

def vocab_file(basename):
    return "prompt-generators/georgian/src/vocab/vocab_lists/" + basename

noun_prompter = VocabPrompter(
    "What is the georgian noun",
    "What is the english noun",
    json_file_name=vocab_file("nouns.json"))

adjective_prompter = VocabPrompter(
    "What is the georgian adjective",
    "What is the english adjective",
    json_file_name=vocab_file("adjectives.json"))

transient_verb_prompter = VocabPrompter(
    "What is the georgian neutral form for",
    "What is the english for",
    json_file_name=vocab_file("transient_verbs.json"))

phrase_prompter = VocabPrompter(
    "როგორაა ქართულად",
    "How do you say in english",
    json_file_name=vocab_file("phrases.json"))

def generate_vocab_prompt():
    return random.choice([
        noun_prompter,
        adjective_prompter,
        transient_verb_prompter,
        phrase_prompter
    ]).translate_prompt()