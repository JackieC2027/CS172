from bank import BankAccount, Checking, Savings

bankAccountList = []
boolValue = False
while not boolValue:
    innerBoolValue = False
    try:
        print("1. Create Savings Account")
        print("2. Create Checking Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Perform End of Month Operations")
        print("6. Display Savings Accounts")
        print("7. Display Checking Accounts")
        print("8. Display All Accounts")
        print("9. Exit")
        print("Enter your choice: ", end="")
        userOption = int(input())
        print()
        if (userOption < 1) or (userOption > 9):
            print("Invalid choice. Try again.")
    except Exception:
        print("Invalid choice. Try again.")
        
    if userOption == 1:
        try:
            print("Savings Account")
            print("Enter owner's name:", end=" ")
            ownerName = input()
            print("Enter initial balance:", end=" ")
            userBalance = float(input())
            while not innerBoolValue:
                if userBalance <= 0:
                    print("Enter a greater than or equal to zero: ", end="")
                    userBalance = float(input())
                else:
                    innerBoolValue = True
                userAccount = Savings(ownerName, userBalance)
                bankAccountList.append(userAccount)
                print("Account Added")
                print()
        except Exception:
            print("Invalid input: an float value was expected. Try again:")
            
    elif userOption == 2:
            try:
                print("Checking Account")
                print("Enter owner's name:", end=" ")
                ownerName = input()
                print("Enter initial balance:", end=" ")
                userBalance = float(input())
                while not innerBoolValue:
                    if userBalance <= 0:
                        print("Enter a greater than or equal to zero: ", end="")
                        userBalance = float(input())
                    else:
                        innerBoolValue = True
                    userAccount = Checking(ownerName, userBalance)
                    bankAccountList.append(userAccount)
                    print("Account Added")
                    print()
            except Exception:
                print("Invalid input: an float value was expected. Try again:")
                
    elif userOption == 3:
        print("Deposit")
        while not innerBoolValue:
            try:
                print("Enter account number:", end=" ")
                userAccountNumber = int(input())
                for bankUser in bankAccountList:
                    if userAccountNumber == bankUser.getAccountNumber():
                        innerBoolValue = True
                        print("Enter amount to deposit: ", end="")
                        userDeposit = float(input())
                        bankUser.deposit(userDeposit)
                if not innerBoolValue:
                    print("That account number does not exist.\n")
                    innerBoolValue = True
                
            except Exception:
                print("Invalid choice. Try again.")
                
    elif userOption == 4:
        print("Withdraw")
        while not innerBoolValue:
            try:
                print("Enter account number:", end=" ")
                userAccountNumber = int(input())
                for bankUser in bankAccountList:
                    if userAccountNumber == bankUser.getAccountNumber():
                        bankUser.withdraw(userWithdraw)
                        innerBoolValue = True
                        print("Enter amount to withdraw:", end=" ")
                        userWithdraw = float(input())
                if not innerBoolValue:
                    print("That account number does not exist.")
                    innerBoolValue = True
            except Exception:
                print("Invalid choice. Try again.")
                
    elif userOption == 5:
        for userBankAccount in bankAccountList:
            userBankAccount.endOfMonth()
        print("End of month operations have been performed")
        
    elif userOption == 6:
        for userBankAccount in bankAccountList:
            if isinstance(userBankAccount, Savings):
                print(userBankAccount)
                
    elif userOption == 7:
        for userBankAccount in bankAccountList:
            if isinstance(userBankAccount, Checking):
                print(userBankAccount)

    elif userOption == 8:
        for userBankAccount in bankAccountList:
            print(userBankAccount)
            
    elif userOption == 9:
        boolValue = True
        print("Good-Bye!")