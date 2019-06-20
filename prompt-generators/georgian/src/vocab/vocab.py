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

    def verb_prompter(self, verb_type):
        vocab_file_basename = "verbs_" + verb_type + ".json"
        vocab_file_path = self.vocab_file(vocab_file_basename)
        return VocabPrompter(
            "What is the georgian neutral form for",
            "What is the english for",
            json_file_name=vocab_file_path)

    # noinspection PyUnusedLocal
    def generate_prompt(self):
        adjective_prompter = VocabPrompter(
            "What is the georgian adjective",
            "What is the english adjective",
            json_file_name=self.vocab_file("adjectives.json"))

        phrase_prompter = VocabPrompter(
            "როგორაა ქართულად",
            "How do you say in english",
            json_file_name=self.vocab_file("phrases.json"))

        noun_prompters = [
            self.noun_prompter("general"),
            self.noun_prompter("time"),
            self.noun_prompter("food_and_drink"),
            self.noun_prompter("animals"),
            self.noun_prompter("nations")
        ]
        verb_prompters = [
            self.verb_prompter("transient"),
            self.verb_prompter("medial"),
        ]
        other_prompters = [
            phrase_prompter,
            adjective_prompter
        ]
        all_prompters = noun_prompters + verb_prompters + other_prompters

        selected_prompters = verb_prompters

        return random.choice(selected_prompters).translate_prompt()
