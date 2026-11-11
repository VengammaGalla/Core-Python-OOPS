def prime_numbers():
    num = 2
    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1
primes = prime_numbers()
for i in range(10):
    print(next(primes))
def running_total(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total
numbers = [1, 3, 5, 2]
for value in running_total(numbers):
    print(value)