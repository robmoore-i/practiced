from vocab.vocab_prompter import VocabPrompter

phrase_prompter = VocabPrompter(
    "How do you say in english",
    "როგორაა ქართულად",
    json_file_name="prompt-generators/georgian/src/vocab/vocab_lists/phrases.json")

def translate_prompt_phrase():
    return phrase_prompter.translate_prompt()