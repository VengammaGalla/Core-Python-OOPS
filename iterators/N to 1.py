class ReverseNumbers:
    def __init__(self, n):
        self.current = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= 1:
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration
n = int(input("Enter N: "))
obj = ReverseNumbers(n)
for i in obj:
    print(i)