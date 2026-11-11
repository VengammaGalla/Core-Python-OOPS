class EvenNumbers:
    def __init__(self, start, count):
        self.start = start
        self.count = count
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.count:
            raise StopIteration
        number = self.start + (self.current * 2)
        if number % 2 != 0:
            number += 1
        self.current += 1
        return number
numbers = EvenNumbers(3, 5)
print("iter returns self:", iter(numbers) is numbers)
print("Using for loop:")
for value in numbers:
    print(value)
numbers = EvenNumbers(3, 5)
print("Using manual next():")
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
try:
    print(next(numbers))
except StopIteration:
    print("StopIteration: No more numbers")