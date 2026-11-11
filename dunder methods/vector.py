class Vector2D:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        print(Vector2D(self.x+other.x,self.y+other.y))
    def __sub__(self,other):
        print(Vector2D(self.x-other.x,self.y-other.y))
    def __mul__(self,other):
        print(Vector2D(self.x*other.x,self.y*other.y))
    def __str__(self):
        return f"Vector2D({self.x},{self.y})"
    def __repr__(self):
        return f"Vector2D({self.x},{self.y})"
v1=Vector2D(3,4)
v2=Vector2D(1,2)
(v1+v2)
v1-v2
v1*v2
print(repr(v1))
print(repr(v2))
print(str(v1))

