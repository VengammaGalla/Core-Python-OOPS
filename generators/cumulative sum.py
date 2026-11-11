def cumulative_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
        yield total
numbers = [1, 2, 3]
for value in cumulative_sum(numbers):
    print(value)
