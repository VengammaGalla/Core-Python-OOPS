class StringIterator:
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
        else:
            raise StopIteration
text = input("Enter a string: ")
obj = StringIterator(text)
for ch in obj:
    print(ch)