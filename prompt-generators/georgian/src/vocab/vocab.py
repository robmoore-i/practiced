import os
import random
from vocab.vocab_prompter import VocabPrompter

class VocabPromptGenerator:
    def __init__(self, vocab_list_dir):
        self.vocab_list_dir = vocab_list_dir

    def vocab_file(self, basename):
        return os.path.join(self.vocab_list_dir, basename)

    def generate_vocab_prompt(self):
        noun_prompter = VocabPrompter(
            "What is the georgian noun",
            "What is the english noun",
            json_file_name=self.vocab_file("nouns.json"))

        adjective_prompter = VocabPrompter(
            "What is the georgian adjective",
            "What is the english adjective",
            json_file_name=self.vocab_file("adjectives.json"))

        transient_verb_prompter = VocabPrompter(
            "What is the georgian neutral form for",
            "What is the english for",
            json_file_name=self.vocab_file("transient_verbs.json"))

        phrase_prompter = VocabPrompter(
            "როგორაა ქართულად",
            "How do you say in english",
            json_file_name=self.vocab_file("phrases.json"))

        return random.choice([
            noun_prompter,
            adjective_prompter,
            transient_verb_prompter,
            phrase_prompter
        ]).translate_prompt()

prompt_generator = VocabPromptGenerator("prompt-generators/georgian/src/vocab/vocab_lists")

def generate_vocab_prompt():
    return prompt_generator.generate_vocab_prompt()