
def menu():
    #main menu system
    choice = -1
    while choice != 4:
        print("Main Menu\n")
        print("[1] Library")
        print("[2] Customers")
        print("[3] Transactions")
        print("[4] Exit")
        choice = int(input())
        if choice == 1:
            book.menu()
        elif choice == 2:
            customer.menu()
            pass
        elif choice == 3:
            transaction.menu()
            pass
        elif choice == 4:
            print("Program exited.\n")
        else:
            print("Error, please try again.\n")


def main():
    
    
    for i in book.Books:
        session.add(i)
 
    session.commit()

    books = session.query(book).all()

    print("All books")
    
    for book1 in books:
        one = "Title: " + book1.title + " Author: " + book1.author + " Category: " + book1.category

    session.close()
    return jsonify("hi")




#https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/
#http://localhost:5000/ping
