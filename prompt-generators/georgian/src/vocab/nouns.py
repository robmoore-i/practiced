from vocab.vocab_prompter import VocabPrompter

noun_prompter = VocabPrompter(
    "What is the georgian noun",
    "What is the english noun",
    json_file_name="prompt-generators/georgian/src/vocab/vocab_lists/nouns.json")

def translate_prompt_noun():
    return noun_prompter.translate_prompt()