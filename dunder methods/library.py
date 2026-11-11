class Library:
    def __init__(self, books):
        self.books = books
    def __len__(self):
        return len(self.books)
    def __contains__(self, title):
        return title in self.books
    def __str__(self):
        return "Library with " + str(len(self.books)) + " books"
# Library with books
library = Library(["Python", "Java", "HTML"])
print(len(library))                  # __len__
print("Python" in library)           # __contains__
print("C++" in library)              # __contains__
print(library)                       # __str__
# Empty library
empty_library = Library([])
print(len(empty_library))
print(bool(empty_library))
print(empty_library)