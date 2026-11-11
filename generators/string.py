def characters(text):
    for ch in text:
        yield ch
text = input("Enter string: ")
for ch in characters(text):
    print(ch)