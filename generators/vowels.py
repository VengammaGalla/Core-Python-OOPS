def vowels(text):
    for ch in text:
        if ch in "aeiouAEIOU":
            yield ch
text = input("Enter string: ")
for ch in vowels(text):
    print(ch)