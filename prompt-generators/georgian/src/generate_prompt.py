import random
from vocab.vocab import generate_vocab_prompt

def generate_prompt():
    prompt_generators = [generate_vocab_prompt]
    prompt_generator = random.choice(prompt_generators)
    return prompt_generator()

def prompt_text(prompt):
    return str(prompt).replace("\"", "\\\"").replace("\\\'", "^").replace("'", "\"").replace("^", "\'")

def get_printed_output():
    return prompt_text(generate_prompt())
