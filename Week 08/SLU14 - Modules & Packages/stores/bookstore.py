
# Description variable
description = "This is a module named bookstore."

# Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}."

# Function to calculate total price
def get_total_price(books):
    return sum(book.price for book in books)
