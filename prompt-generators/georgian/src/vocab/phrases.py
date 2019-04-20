import random

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

def translate_prompt_phrase():
    random_index = random.choice([i for i in range(0, len(phrases))])
    (en, ge) = list(phrases.items())[random_index]
    return {
        "prompt": "როგორაა ქართულად \"" + en + "\"?",
        "answer": ge
    }