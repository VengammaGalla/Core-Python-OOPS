# create a custom iterator that takes list of numbers and returns the current highest
class List:
    def __init__(self,l):
        self.l=l
        self.index=0
        self.m=l[0]
    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.l):
            i=self.index
            # i=max(self.l[self.index+1])
            self.index+=1
            if self.l[i]>self.m:
                self.m=self.l[i]
            return self.m
        raise StopIteration
l=List([10,2,8,9,16,35])
for i in l:
    print(i)
