import random
from transient_verbs import transient_verb_prompt_generators, transient_verbs
from software_pidgin import software_pidgin_prompt_generators

def generate_prompt():
    prompt_generators = transient_verb_prompt_generators + software_pidgin_prompt_generators
    prompt_generator = random.choice(prompt_generators)
    return prompt_generator()

def prompt_text(prompt):
    return str(prompt).replace("\"", "\\\"").replace("'", "\"")

def get_printed_output():
    return prompt_text(generate_prompt())
