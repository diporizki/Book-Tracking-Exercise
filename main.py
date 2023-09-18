from fastapi import FastAPI
from .book_model import Book
from .book_repository import BookRepository

app = FastAPI()

@app.get("/books/")
def get_books():
    return BookRepository.get_books()

@app.post("/book/")
def add_book(book: Book):
    return BookRepository.add_book(book)

# Similar routes for updating and deleting.
