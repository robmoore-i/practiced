import os
import random
from vocab.vocab_prompter import VocabPrompter

class VocabPromptGenerator:
    def __init__(self, vocab_list_dir):
        self.vocab_list_dir = vocab_list_dir

    def vocab_file(self, basename):
        return os.path.join(self.vocab_list_dir, basename)
    
    def noun_prompter(self, noun_type):
        vocab_file_basename = "nouns_" + noun_type + ".json"
        vocab_file_path = self.vocab_file(vocab_file_basename)
        return VocabPrompter(
            "What is the georgian noun",
            "What is the english noun",
            json_file_name=vocab_file_path)

    def generate_prompt(self):
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
            self.noun_prompter("general"),
            self.noun_prompter("time"),
            self.noun_prompter("food_and_drink"),
            self.noun_prompter("animals"),
            self.noun_prompter("nations"),
            adjective_prompter,
            transient_verb_prompter,
            phrase_prompter
        ]).translate_prompt()