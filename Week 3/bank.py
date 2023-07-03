from abc import ABC, abstractmethod

class BankAccount(ABC):
    __nextAccountNumber = 1000
    def __init__(self, owner, balance = 0.0):
        self.__owner = owner
        self.__balance = balance
        self.__accountNumber = BankAccount.__nextAccountNumber
        BankAccount.__nextAccountNumber += 1
        
    def getOwner(self):
        return self.__owner
    
    def getBalance(self):
        return self.__balance
    
    def getAccountNumber(self):
        return self.__accountNumber
    
    def deposit(self, increasedBalanced):
        self.__balance += increasedBalanced
        
    def withdraw(self, decreasedBalanced):
        if decreasedBalanced <= self.__balance:
            self.__balance -= decreasedBalanced
        else:
            print("Not enough balance.")
      
    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.__accountNumber == other.getAccountNumber()
        else:
            return False
        
    @staticmethod
    def getNextAccountNumber():
        return BankAccount.__nextAccountNumber
    
    @abstractmethod
    def endOfMonth():
        pass
    
    def __str__(self):
        myStr = "Account Number: " + str(self.__accountNumber) +"\n"
        myStr += "Account Owner: " + str(self.__owner) +"\n"
        myStr += f"Account Balance: ${self.__balance:.2f}" +"\n"
        return myStr
    
class Savings(BankAccount):
    def __init__(self, owner, balance = 0, interestRate = 3.25):
        super().__init__(owner, balance)
        self.__interestRate = interestRate
        
    def getInterestRate(self):
        return self.__interestRate
    
    def setInterestRate(self, interestValue):
        self.__interestRate = interestValue
        
    def endOfMonth(self):
        monthlyInterest = super().getBalance() * (self.__interestRate/1200)
        super().deposit(monthlyInterest)
        
    def __eq__(self, other):
        if isinstance(other, Savings):
            return super().__eq__(other) and self.__interestRate == other.getInterestRate()
        else:
            return False
        
    def __str__(self):
        myStr = "Account Number: " + str(super().getAccountNumber()) +"\n"
        myStr += "Account Owner: " + str(super().getOwner()) +"\n"
        myStr += f"Account Balance: ${super().getBalance():.2f}" +"\n"
        myStr += f"Annual Interest Rate: {self.__interestRate:.02f}%"
        return myStr

class Checking(BankAccount):
    def __init__(self, owner, balance=0):
        super().__init__(owner, balance)
        self.__transactions = 0
        
    def getTransactionsNum(self):
        return self.__transactions
    
    def deposit(self, increasedBalanced):
        super().deposit(increasedBalanced)
        self.__transactions += 1
        
    def withdraw(self, decreasedBalanced):
        super().withdraw(decreasedBalanced)
        self.__transactions += 1
        
    def endOfMonth(self):
        if self.__transactions > 7:
            super().withdraw(5)
        self.__transactions = 0
        
    def __eq__(self, other):
        return super().getOwner() == other.getOwner()
    
    def __str__(self):
        myStr = "Account Number: " + str(super().getAccountNumber()) +"\n"
        myStr += "Account Owner: " + str(super().getOwner()) +"\n"
        myStr += f"Account Balance: ${super().getBalance():.2f}" +"\n"
        myStr += f"Transactions this month: {self.__transactions}"
        return myStr