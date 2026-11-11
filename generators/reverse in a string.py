def reverse_characters(text):
    for i in range(len(text) - 1, -1, -1):
        yield text[i]
text = input("Enter string: ")
for ch in reverse_characters(text):
    print(ch)