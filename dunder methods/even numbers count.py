class EvenNumbers:
    def __init__(self, start, count):
        self.start = start
        self.count = count
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.count:
            value = self.start

            if value % 2 != 0:
                value = value + 1

            self.start = value + 2
            self.current = self.current + 1

            return value
        else:
            raise StopIteration


# Create iterator
e = EvenNumbers(5, 5)

# Demonstrate with for loop
print("Using for loop:")
for i in e:
    print(i)


# Create another iterator for manual next()
e = EvenNumbers(5, 5)

print("Using next():")
print(next(e))
print(next(e))
print(next(e))
print(next(e))
print(next(e))


# Verify __iter__ returns self
e = EvenNumbers(10, 3)

print("e is iter(e):", e is iter(e))