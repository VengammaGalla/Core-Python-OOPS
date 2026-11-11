class Words:
    def __init__(self, sentence):
        self.words = sentence.split()
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.words):
            word = self.words[self.index]
            self.index += 1
            return word
        raise StopIteration
sentence = "Python is very easy"
obj = Words(sentence)
for word in obj:
    print(word)