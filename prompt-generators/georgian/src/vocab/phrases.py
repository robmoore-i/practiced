from vocab.vocab_prompter import VocabPrompter

phrases = {
    "It depends": "გააჩნია",
    "What does it cost?": "რა ღირს",
    "I don't know": "არ ვიცი",
    "I don't understand": "არ მესმის",
    "I agree with you": "გეთანხმებით",
    "I think so": "ასე ვფიქრობ",
    "I like it": "მომწონს",
    "I prefer it": "მირჩევნია"
}

phrase_prompter = VocabPrompter(phrases, "How do you say in english", "როგორაა ქართულად")

def translate_prompt_phrase():
    return phrase_prompter.translate_prompt()