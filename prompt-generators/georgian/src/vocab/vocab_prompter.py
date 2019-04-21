import random

class VocabPrompter:
    def __init__(self, vocab_list, keyside_question, valueside_question):
        self.vocab_list = vocab_list
        self.keyside_question = keyside_question
        self.valueside_question = valueside_question
    
    def random_vocab(self):
        return random.choice(list(self.vocab_list.keys()))
    
    def translate_prompt(self):
        word = self.random_vocab()
        given, answer, question = random.choice([
            (word,                  self.vocab_list[word], self.keyside_question),
            (self.vocab_list[word], word,                  self.valueside_question)
            ])
        return {
            "prompt": question + " \"" + given + "\"?",
            "answer": answer
        }