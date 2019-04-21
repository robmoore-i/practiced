from vocab.vocab_prompter import VocabPrompter

transient_verb_prompter = VocabPrompter(
    "What is the georgian neutral form for",
    "What is the english for",
    json_file_name="prompt-generators/georgian/src/vocab/vocab_lists/transient_verbs.json")

def translate_prompt_transient_verb():
    return transient_verb_prompter.translate_prompt()
