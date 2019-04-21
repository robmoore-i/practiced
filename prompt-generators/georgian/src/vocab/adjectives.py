from vocab.vocab_prompter import VocabPrompter

adjective_prompter = VocabPrompter(
    "What is the georgian adjective",
    "What is the english adjective",
    json_file_name="prompt-generators/georgian/src/vocab/vocab_lists/adjectives.json")

def translate_prompt_adjective():
    return adjective_prompter.translate_prompt()