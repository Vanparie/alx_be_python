class Book:
    """A class representing a book with title, author, and its availability status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Return whether the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books in a library."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    print(f"Checked out '{title}'")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' not in the library.")

    def return_book(self, title):
        """Return a book by title if it is checked out."""
        for book in self._books:
            if book.title == title:
                if book.return_book():
                    print(f"Returned '{title}'")
                else:
                    print(f"'{title}' was not checked out.")
                return
        print(f"'{title}' not in the library.")

    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")
