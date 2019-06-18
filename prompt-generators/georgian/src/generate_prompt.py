import json
import random
from vocab.vocab import VocabPromptGenerator


class PromptGenerator:
    def __init__(self, georgian_dir):
        self.vocab_prompt_generator = VocabPromptGenerator(georgian_dir + "/src/vocab/vocab_lists")

    def generate_prompt(self):
        return self.vocab_prompt_generator.generate_prompt()

    def get_printed_output(self):
        return json.dumps(self.generate_prompt())
