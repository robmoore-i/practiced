from vocab.vocab_prompter import VocabPrompter

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

adjective_prompter = VocabPrompter(adjectives, "What is the georgian adjective", "What is the english adjective")

def translate_prompt_adjective():
    return adjective_prompter.translate_prompt()