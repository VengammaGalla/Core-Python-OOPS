class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= 0:
            value = self.text[self.index]
            self.index -= 1
            return value
        else:
            raise StopIteration
text = input("Enter a string: ")
obj = ReverseString(text)
for ch in obj:
    print(ch)