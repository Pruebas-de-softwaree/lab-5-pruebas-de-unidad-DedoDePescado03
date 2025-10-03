from library import Library
from book import Book
from user import User

def run():
    test = Library()
    test.add_book(Book("1984", "George Orwell", "1949", "ISBN001"))
    test.add_user(User("Gael", "1"))
    test.add_user(User("Max", "2"))
    test.borrow_book("1","ISBN001")
    test.borrow_book("2","ISBN001")

if __name__ == "__main__":
    run()