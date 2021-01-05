#Customers

from sqlalchemy import Column, Integer, Unicode, Float, String, Sequence
from base import Base



class customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    customer_id = Column(Integer())
    name = Column(String(50))
    balance = Column(Float(50))
    books_out = []
    Customers = []

    def __init__(self, name, balance, customer_id):
        self.name = name
        self.balance = balance
        self.customer_id = customer_id

    def __repr__(self):
        return "<User(customer_id='%i', name='%s', balance='%f')>" % (
                self.customer_id, self.name, self.balance)
    @staticmethod
    def add():
        name = input("Insert Name:")
        balance = input("Insert Balance:")
        customer_id = len(customer.Customers)+1
        new_customer = customer(name, balance, customer_id)
        customer.Customers.append(new_customer)
    @staticmethod
    def delete():
        name = input("Insert Name:")
        for i in customer.Customers:
            if i.name == name:
                    customer.Customers.remove(i)
                    print("Customer has been successfully removed.")
    @staticmethod
    def search():
        name = input("Insert Name:")#prints all books by author in library
        for i in customer.Customers:
            if i.name == name:
                print("Name: " + i.name)
                print("Title: " + i.balance)
                #print("Books Checked Out: " + i.books_out +"\n")
                break
    @staticmethod
    def print_customers():
        for i in customer.Customers:
            print("Name: " + i.name)
            print("Title: " + i.balance)
            #print("Books Checked Out: " + i.books_out +"\n")
    @staticmethod
    def print():
        pass
    @staticmethod
    def edit():
        name = input("Insert Name of Customer:")
        for i in customer.Customers:
            if i.name == name:
                editin = -1
                while editin != 4:
                    print(" [1] Edit Name")
                    print(" [2] Edit Balance")
                    print(" [3] Edit Books Out")
                    print(" [4] Return to Previous Menu")
                    editin = int(input())
                    if editin == 1: #edit customer name
                        name = input("Insert New Name:")
                        i.name = name
                        break
                    elif editin == 2:#edit customer balance
                        balance = int(input("Insert New Balance:"))
                        i.balance = balance
                        break
                    elif editin == 3:#edit customer books out, incomplete##############
                        break
                    elif editin == 4:# return to previous menu
                        break
                    else:
                        print("Error, please try again.\n")
            else:
                print("Invalid name.")
        

    #customer menu option
    @staticmethod
    def menu():
        custInput = -1
        while custInput != 7:
            print("Customer System\n")
            print(" [1] Add Customer")
            print(" [2] Delete Customer")
            print(" [3] Search for Customer")
            print(" [4] Print Customers")
            print(" [5] Print")
            print(" [6] Edit Customer")
            print(" [7] Return to Main Menu")
            custInput = int(input())
            if custInput == 1: #add customer
                customer.add()
            elif custInput == 2:#delete customer
                customer.delete()
            elif custInput == 3:#search for customer
                customer.search()
            elif custInput == 4:# print customers
                customer.print_customers()
                break
            elif custInput == 5:#print
                customer.print()
                break
            elif custInput == 6:#edit customer
                customer.edit()
                break
            elif custInput == 7:# return to main menu
                break
            else:
                print("Error, please try again.\n")