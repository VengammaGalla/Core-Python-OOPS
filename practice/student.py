# Create a class Student with:
# 	attributes: name, marks
# 	method: grade()
# Implement:
# 	_str_()
# 	_add_() → add marks of two students
# 	_truediv_() → divide marks by a number
# 	_ge_() → check if one student scored greater than or equal to another
# 	_lt_() → check if one student scored less
# 	_getattribute_() → track attribute access
# 	_setattr_() → marks must be between 0 and 100

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __str__(self):
        return "Name: " + self.name + ", Marks: " + str(self.marks)
    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"
    def __add__(self,other):
        return self.marks+other.marks
    def __truediv__(self,num):
        return self.marks/num
    def __ge__(self,other):
        return self.marks>=other.marks
    def __lt__(self,other):
        return self.marks<=other.marks
    def __getattribute__(self,name):
        print(f"{name} is accessed")
        return super().__getattribute__(name)
    def __setattr__(self,name,value):
        if name == "marks":
            if value < 0 or value > 100:
                print("Marks must be between 0 and 100")
                return
        object.__setattr__(self, name, value)
s1=Student("Vennela",85)
s2=Student("Anu",70)

print(s1)
print("Grade:",s1.grade())

print("Addition:",s1+s2)
print("Division:",s1/5)

print("s1 >= s2:",s1>=s2)
print("s1 < s2:",s1<s2)

s1.marks=95
print(s1)

s1.marks=120