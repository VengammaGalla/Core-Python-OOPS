def squares(numbers):
    for num in numbers:
        yield num * num
numbers = [1, 2, 3, 4, 5]
for value in squares(numbers):
    print(value)