class EvenList:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            if value % 2 == 0:
                return value
        raise StopIteration
numbers = [10, 15, 20, 25, 30, 35]
obj = EvenList(numbers)
for i in obj:
    print(i)