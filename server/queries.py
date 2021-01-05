from library import book
from customers import customer
from transactions import transaction
from base import Session

def ping():
    session = Session()
    books = session.query(book).all()

    print("All books")

    for book in books:
        print(f'Title: {book.title} Author: {book.author} Category: {book.category}')
    print('')

    return jsonify("all")