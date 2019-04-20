import random

adjectives = {
    "good": "კარგი",
    "bad": "ცუდი",
    "pleasant": "სასიამოვნო",
    "big": "დიდი",
    "little": "პატარა",
    "important": "მნიშვნელოვანია",
    "expensive": "ძვილი",
    "cheap": "იაფი",
    "cold": "ცივი",
    "hot": "ცხელი",
    "new": "ახალო",
    "old": "ძველი",
    "beautiful": "ლამაზი",
    "easy": "ადვილი",
    "difficult": "რთული",
    "tall": "მაღალი",
    "young": "ახალგაზრდა",
    "clever": "ჭკვიანი",
    "strong": "ძლიერი",
    "weak": "სუსტი",
    "happy": "ბედნიერი",
    "soon": "მალე",
    "already": "ეკვე",
    "together": "ერთად",
    "often": "ხშირად",
    "early": "ადრე",
    "late": "გვიან"
}

def random_adjective():
    return random.choice(list(adjectives.keys()))

def translate_prompt_adjective_ge_en():
    adjective = random_adjective()
    return {
        "prompt": "What is the english adjective \"" + adjectives[adjective] + "\"?",
        "answer": adjective
    }

def translate_prompt_adjective_en_ge():
    adjective = random_adjective()
    return {
        "prompt": "What is the georgian adjective \"" + adjective + "\"?",
        "answer": adjectives[adjective]
    }

def translate_prompt_adjective():
    return random.choice([
        translate_prompt_adjective_ge_en,
        translate_prompt_adjective_en_ge
    ])()
