def digits(text):
    for ch in text:
        if ch.isdigit():
            yield ch
text = input("Enter string: ")
for ch in digits(text):
    print(ch)