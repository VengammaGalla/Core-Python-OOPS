class NumberRange:
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    # (a) len()
    def __len__(self):
        count = 0
        value = self.start

        if self.step > 0:
            while value < self.stop:
                count = count + 1
                value = value + self.step
        else:
            while value > self.stop:
                count = count + 1
                value = value + self.step

        return count

    # (b) x in range
    def __contains__(self, x):
        if self.step > 0:
            if x < self.start or x >= self.stop:
                return False
        else:
            if x > self.start or x <= self.stop:
                return False

        return (x - self.start) % self.step == 0

    # (c) Iterable
    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.step > 0:
            if self.current >= self.stop:
                raise StopIteration
        else:
            if self.current <= self.stop:
                raise StopIteration

        value = self.current
        self.current = self.current + self.step

        return value

    # (d) __str__
    def __str__(self):
        return "NumberRange(" + str(self.start) + ", " + str(self.stop) + ", " + str(self.step) + ")"

    # (d) __repr__
    def __repr__(self):
        return "NumberRange(" + str(self.start) + ", " + str(self.stop) + ", " + str(self.step) + ")"

    # (e) + operator
    def __add__(self, other):
        result = []

        for value in self:
            result.append(value)

        for value in other:
            result.append(value)

        return result


# Create objects
r1 = NumberRange(1, 10, 2)
r2 = NumberRange(10, 15, 2)

# (a) Test len()
print("Length:", len(r1))

# (b) Test __contains__
print("5 in r1:", 5 in r1)
print("6 in r1:", 6 in r1)

# (c) Test iteration
print("Values:")
for value in r1:
    print(value, end=" ")

print()

# (d) Test __str__ and __repr__
print("String:", str(r1))
print("Representation:", repr(r1))

# (e) Test +
print("Combined list:", r1 + r2)