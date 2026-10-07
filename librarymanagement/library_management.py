class Book:

    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} added to the library")

    def remove_book(self, isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_remove = book
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book {book_to_remove.title} removed from the library")

    def display_books(self):
        if not self.books:
            print("No books in the library")
        else:
            for book in self.books:
                book.display_info()

class SpecialLibrary(Library):
    def add_book(self, book):
        super().add_book(book)
        print(f"Special handling for the book {book.title}")

book1 = Book("Azure OpenAI", "Bharat", "123")
book2 = Book("AWS Lambda", "Manoj", "456")

library = Library()

library.add_book(book1)
library.add_book(book2)

library.display_books()

library.remove_book("123")
library.display_books()

special_library = SpecialLibrary()
special_library.add_book(book1)
