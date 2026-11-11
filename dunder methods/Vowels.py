# create custom iterator that returns vowels from the given string
class Vowels:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            i=self.l[self.index]
            self.index+=1
            if i in "AEIOUaeiou":
                return i
        raise StopIteration
v=Vowels("VHello world")
# it=iter(v)
for i in v:
    print(i)


