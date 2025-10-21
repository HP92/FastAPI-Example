# The tutorial which was used.
# https://realpython.com/get-started-with-fastapi/#create-the-most-minimal-fastapi-app

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

books = [
    { "id": 1, "title": "Python Basics", "author": "Real P.", "pages": 635 },
    { "id": 2, "title": "Breaking the Rules", "author": "Stephen G.", "pages": 99 },
    { "id": 3, "title": "Lord of the Rings", "author": "J.R.R.Tolkien", "pages": 700 }
]

class Book(BaseModel):
    title: str
    author: str
    pages: int

@app.get("/")
def index():
    return { "message": "Hello World! Hello Fast API" }

@app.get("/books")
def get_books(limit: int | None = None):
    """ Get all books, optionally limited by count. """
    if limit:
        return { "books": books[:limit] }
    return { "books": books }

@app.get("/books/{book_id}")
def get_book(book_id: int):
    """ Get specific book by ID. """
    for book in books:
        if book["id"] == book_id:
            return book
    
    return { "error": "Book not found" }


@app.post("/books")
def create_book(book: Book):
    new_book = {
        "id": len(books) + 1,
        "title": book.title,
        "author": book.author,
        "pages": book.pages
    }

    books.append(new_book)
    return new_book

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)