class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            raise ValueError("The book is already borrowed")
        print(f"Borrowed book {self.title}")
        self.borrowed = True

    def return_book(self):
        if not self.borrowed:
            raise ValueError("The book is not currently borrowed")
        print(f"The book {self.title} has been returned")
        self.borrowed = False


