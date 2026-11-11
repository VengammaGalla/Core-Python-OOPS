class Book:
    total_books=0
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        Book.total_books+=1
    @classmethod
    def from_string(cls,book_str):
            title,author=book_str.split("-")
            if cls.is_valid_title(title):
                return cls(title,author)
            else:
                return "Invalid book title"
    @staticmethod
    def is_valid_title(title):
        return len(title)>3
b1=Book("venni","james")
print(b1.title,b1.author)
# b2=Book.is_valid_title("java-python")
b2=Book.from_string("python-java")
print(b2.title,b2.author)
