class Noun:
    def __init__(self, en, ge):
        self.en = en
        self.ge = ge

    def accusative_ge(self):
        return self.ge[:-1] + "ს"

CODE = Noun("code", "კოდი")
BOOK = Noun("a book", "წიგნი")