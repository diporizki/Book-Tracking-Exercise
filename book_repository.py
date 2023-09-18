from typing import List
from .book_model import Book

class BookRepository:
    books: List[Book] = []

    @classmethod
    def get_books(cls):
        return cls.books

    @classmethod
    def add_book(cls, book: Book):
        cls.books.append(book)
        return book

    # Similarly, you can add `update_book_status` and `delete_book`.
