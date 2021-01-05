#Library self.books
from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Sequence
from base import Base

class book(Base):
    __tablename__ = 'books'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    author = Column(String(50))
    title = Column(String(50))
    category = Column(String(50))
    book_id = Column(Integer())
    Books = []
    def __init__(self, author, title, category, book_id):
        self.author = author
        self.title = title
        self.category = category
        self.book_id = book_id

    def __repr__(self):
        return "<User(author='%s', title='%s', category='%s')>" % (
                self.author, self.title, self.category)
    @staticmethod
    def add():
        author = input("Insert Author:")
        title = input("Insert Title:")
        category = input("Insert Category:")
        book_id = len(book.Books)+1
        new_book = book(author, title, category, book_id)
        print("Book has been added.\n")
        book.Books.append(new_book)
    @staticmethod
    def delete():
        author = input("Insert Author:")
        title = input("Insert Title:")
        for i in book.Books:
            if i.author == author:
                if i.title == title:
                    book.Books.remove(i)
                    print("Book has been successfully removed.")
    @staticmethod       
    def search():
        author = input("Insert Author:")#prints all self.books by author in library
        for i in range(0,len(book.Books)):
            if book.Books[i].author == author:
                print("Author: " + book.Books[i].author)
                print("Title: " + book.Books[i].title)
                print("Category: " + book.Books[i].category +"\n")
    @staticmethod
    def print_books():
        for i in range(0,len(book.Books)):
            print("Author: " + book.Books[i].author)
            print("Title: " + book.Books[i].title)
            print("Category: " + book.Books[i].category)
            print("ID: " + str(book.Books[i].book_id) + "\n")
    @staticmethod
    def edit():
        editin = -1
        while editin != 4:
            print(" [1] Edit Author")
            print(" [2] Edit Title")
            print(" [3] Category")
            print(" [4] Return to Previous Menu")
            editin = int(input())
            if editin == 1: #edit author
                editauthor = input("Insert Author:")
                for i in range(0,len(book.Books)):
                    if book.Books[i].author == editauthor:
                        break
                break
            elif editin == 2:#edit title
                edittitle = input("Insert Title:")
                for i in range(0,len(book.Books)):
                    break
                break
            elif editin == 3:#edit category
                editcategory = input("Insert Category:")
                for i in range(0,len(book.Books)):
                    break
                break
            elif editin == 4:# return to previous menu
                break
            else:
                print("Error, please try again.\n")
            

    #menu selection function
    @staticmethod
    def menu():
        libinput = -1
        while libinput != 8:
            print("Library System\n")
            print(" [1] Add Item")
            print(" [2] Delete Item")
            print(" [3] Search for Item")
            print(" [4] Print Books")
            print(" [5] Print")
            print(" [6] Edit Loan")
            print(" [7] Report Lost")
            print(" [8] Return to Main Menu")
            libinput = int(input())
            if libinput == 1: #add item
                book.add()     
            elif libinput == 2:#delete item
                book.delete()
            elif libinput == 3:#search for item
                book.search()
            elif libinput == 4:# prints all self.books, possibly add print by category, figure out how to sort
                book.print_books()
            elif libinput == 5:#print
                break
            elif libinput == 6:#edit
                book.edit()
            elif libinput == 7:#report lost
                break
            elif libinput == 8:# return to main menu
                break
            else:
                print("Error, please try again.\n")