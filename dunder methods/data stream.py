class DataStream:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = 0

    # (1) Full iterator
    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data_list):
            value = self.data_list[self.index]
            self.index = self.index + 1
            return value
        else:
            raise StopIteration

    # (2) len()
    def __len__(self):
        return len(self.data_list)

    # (2) 'in' operator
    def __contains__(self, value):
        return value in self.data_list

    # (3) + operator
    def __add__(self, other):
        return DataStream(self.data_list + other.data_list)

    # (4) __str__
    def __str__(self):
        return str(self.data_list)

    # (4) __repr__
    def __repr__(self):
        return "DataStream(" + str(self.data_list) + ")"

    # (5) map()
    def map(self, func):
        for value in self.data_list:
            yield func(value)

    # (6) filter()
    def filter(self, pred):
        for value in self.data_list:
            if pred(value):
                yield value


# Create a stream
stream = DataStream([1, 2, 3, 4, 5, 6])

# Test len()
print("Length:", len(stream))

# Test 'in'
print("4 in stream:", 4 in stream)
print("10 in stream:", 10 in stream)

# Test str()
print("String:", str(stream))

# Test repr()
print("Representation:", repr(stream))

# Filter even numbers
even_numbers = stream.filter(lambda x: x % 2 == 0)

# Map even numbers to squares
squares = stream.map(lambda x: x * x)

print("Even numbers:", list(even_numbers))
print("Squares:", list(squares))

# Test + operator
stream2 = DataStream([7, 8, 9])
combined = stream + stream2

print("Combined:", combined)

# Test iterator
print("Iterator values:")
for value in stream:
    print(value, end=" ")