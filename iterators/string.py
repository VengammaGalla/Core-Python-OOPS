class Characters:
    def __init__(self, text):
        self.text = text
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.text):
            value = self.text[self.index]
            self.index += 1
            return value
        raise StopIteration
text = input("Enter a string: ")
for ch in Characters(text):
    print(ch)