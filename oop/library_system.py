class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call the base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"{super().__str__()} - Size: {self.file_size} KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call the base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} - Pages: {self.page_count}"


class Library:
    def __init__(self):
        self.books = []  # List to store instances of Book, EBook, and PrintBook

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        print("Books in the Library:")
        for book in self.books:
            print(book)
