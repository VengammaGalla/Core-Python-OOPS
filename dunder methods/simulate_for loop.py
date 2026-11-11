def simulate_for_loop(iterable):
    it = iter(iterable)
    index = 0

    while True:
        try:
            value = next(it)
            print(index, "->", value)
            index = index + 1
        except StopIteration:
            break


# List
print("List:")
simulate_for_loop([10, 20, 30, 40])

# String
print("String:")
simulate_for_loop("Python")

# Range
print("Range:")
simulate_for_loop(range(1, 6))