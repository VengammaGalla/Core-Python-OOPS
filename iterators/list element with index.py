class IndexedList:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.numbers):
            result = (self.index, self.numbers[self.index])
            self.index += 1
            return result
        raise StopIteration
numbers = [10, 20, 30, 40]
obj = IndexedList(numbers)
for index, value in obj:
    print(index, value)