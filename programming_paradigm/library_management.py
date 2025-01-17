class Book:
    """Class to represent a book in the library."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

    def is_available(self) -> bool:
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Class to represent a library."""
    def __init__(self):
        self._books = []

    def add_book(self, book: Book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title: str) -> str:
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return f"'{title}' has been checked out."
                return f"'{title}' is already checked out."
        return f"'{title}' is not in the library."

    def return_book(self, title: str) -> str:
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return f"'{title}' has been returned."
                return f"'{title}' was not checked out."
        return f"'{title}' is not in the library."

    def list_available_books(self) -> str:
        """List all available books in the library."""
        available_books = [f"{book.title} by {book.author}" for book in self._books if book.is_available()]
        if available_books:
            return "Available books:\n" + "\n".join(available_books)
        return "No books are currently available."

