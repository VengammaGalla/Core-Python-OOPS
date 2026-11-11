def numbers(n):
    for i in range(1, n + 1):
        yield i
n = numbers(10)
for i in n:
    print(i)