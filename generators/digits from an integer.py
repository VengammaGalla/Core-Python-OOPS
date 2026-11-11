def integer_digits(num):
    for digit in str(num):
        yield int(digit)
num = int(input("Enter number: "))
for digit in integer_digits(num):
    print(digit)