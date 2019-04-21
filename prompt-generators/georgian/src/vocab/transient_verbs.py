from vocab.vocab_prompter import VocabPrompter

transient_verbs = {
    "help": "ეხმარებ",
    "eat": "ჭამ",
    "drink": "სვამ",
    "buy": "ყიდულობ",
    "add": "ამატებ",
    "build": "აშენებ",
    "work": "მუშაობ",
    "write": "წერ",
    "see": "ხედავ",
    "read": "კითხულობ",
    "sell": "ყიდი",
    "travel": "მგზავრობ",
    "study": "სწავლობ"
}

transient_verb_prompter = VocabPrompter("What is the georgian neutral form for", "What is the english for", vocab_list=transient_verbs)

def translate_prompt_transient_verb():
    return transient_verb_prompter.translate_prompt()
