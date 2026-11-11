def prime_numbers():
    n = 2

    while True:
        c = 0

        for i in range(1, n + 1):
            if n % i == 0:
                c = c + 1

        if c == 2:
            yield n

        n = n + 1


# Print first 10 prime numbers
p = prime_numbers()

print("First 10 prime numbers:")
for i in range(10):
    print(next(p), end=" ")


def running_total(numbers):
    total = 0

    for i in numbers:
        total = total + i
        yield total


print("\nRunning total:")
for value in running_total([1, 3, 5, 2]):
    print(value, end=" ")