class OddNumbers:

    def __init__(self, n):
        self.n = n
        self.count = 0
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            value = self.current
            self.current += 2
            self.count += 1
            return value
        else:
            raise StopIteration


n = int(input("Enter N: "))

obj = OddNumbers(n)

for i in obj:
    print(i)
    