class PositiveNumbers:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.numbers):
            value = self.numbers[self.index]
            self.index += 1
            if value > 0:
                return value
        raise StopIteration
numbers = [-5, 10, -2, 20, 0, 30, -7]
obj = PositiveNumbers(numbers)
for i in obj:
    print(i)