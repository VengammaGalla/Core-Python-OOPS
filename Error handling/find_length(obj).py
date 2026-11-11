def find_length(obj):
    count = 0
    try:
        for item in obj:
            count += 1
        return count
    except TypeError:
        print("Error: Integer is not iterable")

print(find_length("Python"))
print(find_length([10, 20, 30]))
print(find_length(100))