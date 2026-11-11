class LibraryMember:
    total_members = 0
    limit = 2
    def __init__(self, name):
        self.name = name
        self.books = 0
        LibraryMember.total_members += 1
    def borrow(self, title):
        if LibraryMember.check(title):
            if self.books < LibraryMember.limit:
                self.books += 1
                print(self.name, "borrowed", title)
            else:
                print("Borrow limit reached")
        else:
            print("Invalid book title")
    @classmethod
    def change_limit(cls, new_limit):
        cls.limit = new_limit
    @staticmethod
    def check(title):
        return title != ""
# Creating members
m1 = LibraryMember("Ravi")
m2 = LibraryMember("Sneha")

print("Total Members:", LibraryMember.total_members)

# Borrow books
m1.borrow("Python")
m1.borrow("Java")
m2.borrow("C")

# Invalid title
m2.borrow("")

# Change borrowing limit
LibraryMember.change_limit(3)

# Borrow again
m1.borrow("HTML")

print("Ravi Books:", m1.books)
print("Sneha Books:", m2.books)