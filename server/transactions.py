#Transactions

from sqlalchemy import Column, Integer, Unicode, Float, String, Sequence
import library
from sqlalchemy.ext.declarative import declarative_base
from base import Base


class transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    book_id = Column(Integer())
    customer_id = Column(Integer())
    cost = Column(Float(100))
    due_date = Column(String(50))
    status = Column(String(20))
    Transactions = []
    def __init__(self, book_id, customer_id, due_date):
        self.book_id = book_id
        self.customer_id = customer_id
        self.due_date = due_date
    def __repr__(self):
        return "<User(id='%i',book_id='%i',customer_id='%i',cost='%f',due_date='%i',status='%s')>" % (
                self.id, self.book_id, self.customer_id, self.cost, self.due_date, self.status)
    @staticmethod
    def CheckOut():
        book_id = input("Insert Book ID:")
        customer_id = input("Insert Customer ID:")
        due_date = 0
        #for i in Books:
           # break
        new_transaction = transaction(book_id, customer_id, due_date)
        transaction.Transactions.append(new_transaction)
        pass
    @staticmethod
    def CheckIn():
        pass
    @staticmethod
    def ListOverdue():
        pass
    @staticmethod
    def ListBooks():
        pass
    @staticmethod
    def UpdateStatus():
        pass
    @staticmethod
    def ReCheck():
        pass
    @staticmethod
    def EditLoan():
        pass
    @staticmethod
    def ReportLost():
        pass
    @staticmethod
    def menu():
        tranInput = -1
        while tranInput != 9:
            print("Transaction System\n")
            print(" [1] Check Out")
            print(" [2] Check In")
            print(" [3] List Overdue")
            print(" [4] List Books")
            print(" [5] Update Status")
            print(" [6] Recheck Out")
            print(" [7] Edit Loan")
            print(" [8] Report Lost")
            print(" [9] Return to Main Menu")
            tranInput = int(input())
            if tranInput == 1: #check out
                transaction.CheckOut()
            elif tranInput == 2:#check in
                transaction.CheckIn()
            elif tranInput == 3:#list overdue
                transaction.ListOverdue()
            elif tranInput == 4:#list books
                transaction.ListBooks()
                break
            elif tranInput == 5:#update status
                transaction.UpdateStatus()
                break
            elif tranInput == 6:#Recheck out
                transaction.ReCheck()
                break
            elif tranInput == 7:#Edit Loan
                transaction.EditLoan()
                break
            elif tranInput == 8:#Report Loan
                transaction.ReportLost()
                break
            elif tranInput == 9:# return to main menu
                break
            else:
                print("Error, please try again.\n")