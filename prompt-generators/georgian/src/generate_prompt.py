import random
from transient_verbs import translate_prompt_transient_verb
from software_pidgin import translate_prompt_programming

def generate_prompt():
    prompt_generators = [translate_prompt_transient_verb, translate_prompt_programming]
    prompt_generator = random.choice(prompt_generators)
    return prompt_generator()

def prompt_text(prompt):
    return str(prompt).replace("\"", "\\\"").replace("'", "\"")

def get_printed_output():
    return prompt_text(generate_prompt())
