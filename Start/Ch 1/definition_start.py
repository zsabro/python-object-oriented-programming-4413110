# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Book():
    def __init__ (self, title):
        self.title = title
    print("This is the book class")
    print("Being tested that what prints on the next lines after calling the initializer")

# TODO: create instances of the class
book1 = Book("War and Peace")
book2 = Book("Cindrella")

# TODO: print the class and property
print(book1)
print(book1.title)

print(book2)
print(book2.title)