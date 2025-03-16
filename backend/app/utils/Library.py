from utils.book import Book

class Library:

    def __init__(self):
        self.books = []


    def book_inventory(self):
        return (len(self.books))

    def book_inventory(self):
        return len(self.books), self.books

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed from the library.")
                return
        print(f"Book with ID {book_id} not found.")

    def display_books(self):
        if not self.books:  # if the library is empty
            print("No books available in the library.")
        else:
            for book in self.books:
                print(f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Quantity: {book.quantity}")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(
                    f"Found book: ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Quantity: {book.quantity}")
                return
        print(f"Book titled '{title}' not found.")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.quantity > 0:
                    book.quantity -= 1
                    print(f"Book '{book.title}' issued. Remaining quantity: {book.quantity}")
                else:
                    print(f"Book '{book.title}' is currently out of stock.")
                return
        print(f"Book with ID {book_id} not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.quantity += 1
                print(f"Book '{book.title}' returned. Updated quantity: {book.quantity}")
                return
        print(f"Book with ID {book_id} not found.")

if __name__ == "__main__":
    lib = Library()

    name = input("Pleaser , Enter the Book Name: ")
    lib.books.append(name)

    name = input("Pleaser , Enter the Book Name: ")
    lib.books.append(name)

    name = input("Pleaser , Enter the Book Name: ")
    lib.books.append(name)

    print(lib.books)
    print(lib.book_inventory())

    # Displaying books
    lib.display_books()
    #
    # # Searching for a book
    # lib.search_book("nkem")
    #
    # # Issuing a book
    # lib.issue_book(1)
    # lib.issue_book(1)
    #
    # # Returning a book
    # lib.return_book(1)
    #
    # # Removing a book
    # lib.remove_book(1)
    #
    # # Displaying books after removal
    # lib.display_books()