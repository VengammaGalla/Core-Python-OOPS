def running_maximum(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
        yield maximum
numbers = [3, 1, 4, 2]
for value in running_maximum(numbers):
    print(value)