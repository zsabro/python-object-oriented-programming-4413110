# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price, discount):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.discount = discount

    # TODO: create instance methods
    def get_price(self):
        return self.price
    
    def discount_price(self, discount):
        print(f"""The price before discount was Rs.{self.price}""")
        self.price = self.price - (self.price * discount)
        print(f"""The price after discount is Rs.{self.price}""")
        return self.price

# TODO: create some book instances
b1 = Book("War and Peace","Leo Tolstoy", 1200, 12000, 0.25)
b2 = Book("The Catcher in the Rye", "Un Known", 136, 560, 0.40)

# TODO: print the price of book1
# print(f"""Book :{b1.title}, Author :{b1.author}, Actual Price Rs.{b1.price} and Pages: {b1.pages}""")
# print(f""" The price is obtained through the 'Python_method' is : {b1.get_price()}""")

# TODO: try setting the discount
print(b1.discount_price(0.25))

# TODO: properties with double underscores are hidden by the interpreter
