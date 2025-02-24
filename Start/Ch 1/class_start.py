# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances

    # TODO: double-underscore properties are hidden from other classes
    BOOKTYPES = ("HARDCOVER", "PAPERBACK", "E.BOOK")
    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOKTYPES

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        self.booktype = booktype
        if (booktype not in Book.BOOKTYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            print({booktype})


# TODO: access the class attribute
print((" Book types: ", Book.getbooktypes()))

# TODO: Create some book instances
b1 = Book("Angels and Demons", "HARDCOVER")
b2 = Book("Broken Wings", "E.BOOK")

# TODO: Use the static method to access a singleton object
