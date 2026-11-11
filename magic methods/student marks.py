class Student:
    def __init__(self,i,name,marks):
        self.Id=i
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __lt__(self,other):
        return self.marks<other.marks
    def __eq__(self,other):
        return self.marks==other.marks
    def __hash__(self):
        return hash(self.Id)
    def __repr__(self):
        return self.name
s1=Student(10,"x",90)
s2=Student(20,"y",80)
s3=Student(30,"z",70)
s={s1,s2,s3}
print(s)
