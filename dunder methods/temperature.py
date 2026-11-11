class Temperature:
    def __init__(self,celsius):
        self.celsius=celsius
    def __lt__(self,other):
        print(self.celsius<other.celsius)
    def __gt__(self,other):
        print(self.celsius>other.celsius)
t1=Temperature(100)
t2=Temperature(50)
t1<t2
t1>t2

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius

    def __gt__(self, other):
        return self.celsius > other.celsius

    def __ge__(self, other):
        return self.celsius >= other.celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __hash__(self):
        return hash(self.celsius)

    def __str__(self):
        return str(self.celsius)


# Create Temperature objects
t1 = Temperature(100)
t2 = Temperature(50)
t3 = Temperature(75)
t4 = Temperature(50)

# Sorting
temperatures = [t1, t2, t3]
temperatures.sort()

print("Sorted temperatures:")
for t in temperatures:
    print(t)

# Store in set
s = {t1, t2, t3, t4}

print("Set:")
for t in s:
    print(t)

# Verification
print("Temperature(100) > Temperature(50):", t1 > t2)


