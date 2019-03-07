import random
from transient_verbs import transient_verb_generated_prompts, transient_verbs

def translate_prompt():
    potential_prompts = transient_verb_generated_prompts
    return random.choice(potential_prompts)

def prompt_text(prompt):
    return str(prompt).replace("\"", "\\\"").replace("'", "\"")

def get_printed_output():
    return prompt_text(translate_prompt())
