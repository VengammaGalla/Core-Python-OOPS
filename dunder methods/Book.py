class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def __str__(self):
        return f"{self.title} by {self.author} - {self.price}"
    def __repr__(self):
        return f"Book('{self.title}','{self.author}','{self.price}')"
b1=Book("x","venni",500)
print(Book)
print(b1)
print(repr(b1))
print(f"{b1}")
print(f"{b1!r}")
print(str(b1))