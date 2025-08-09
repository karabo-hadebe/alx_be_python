class Book:
    def __init__(self, title: str, author: str):
        """Initialize a book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        """Initialize an eBook with title, author, and file size in KB."""
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        """Initialize a print book with title, author, and page count."""
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize an empty library."""
        self.books = []

    def add_book(self, book: Book):
        """Add a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):  # Ensure only valid book types are added
            self.books.append(book)
        else:
            print("Only Book or its subclasses can be added to the library.")

    def list_books(self):
        """Print details of all books in the library."""
        if not self.books:
            print("The library is empty.")
        for book in self.books:
            print(book)

