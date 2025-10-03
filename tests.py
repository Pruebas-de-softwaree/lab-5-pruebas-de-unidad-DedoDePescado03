from book import Book

def run():
    test = Book("Harry Potter", "J.K Rowling", "1980", "ISBN001")
    test.borrow()

if __name__ == "__main__":
    run()