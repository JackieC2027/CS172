# Programmers: Jackie Cheng and Noel Aniyankunju
# Date: 5/18/23
# Purpose: Using OOP and stackclass.py, this program simulates a calculator that
# takes postfix notation for calculations. Stacking with an empty stack, using the push and pop
# methods of the Stack, I can add the values to the stack, given that they are not one of the operators
# and produce a simple script that allows users to use the calculator in the terminal.
# Intially, I chose a isdigit approach to check each operator, but I later referred to the notes
# and realized that isdigit does not work for negative integers, a test case that I was failing.

from stackclass import Stack
def postfix(exp):
    '''
    Function: postfix(exp)
    Purpose: Takeing the string expression of a calculation and computes the value of the postfix expression.
    Parameters:
    exp: a string value that holds the postfix notation for the expression
    Return Value: returns the popped value from the Stack after the calculations
    Usage: postfix(userExpression)
    '''
    splitExpression = exp.split(" ") #Splits the expression by each space
    calculatorStack = Stack() #Creates an empty stack
    for value in splitExpression: #Loops through each item in the split expression
        if value != "+" and value != "-" and value != "/" and value != "*":
            #The above expression checks if the value at the given index is one of the intended operators of the calculator
            calculatorStack.push(value) #Not an operator, push the value into the stack
            
        else:
            '''
            Since the second item popped off the
            top came before the top item in the
            postfix statement, it is the left operand.
            '''
            rightDigit = float(calculatorStack.pop()) 
            leftDigit = float(calculatorStack.pop())
            if value == "+": #Addition operator
                calculatorStack.push(leftDigit + rightDigit) #Pushes computed value to the top of the stack
                
            elif value == "*": #Multiplication
                calculatorStack.push(leftDigit * rightDigit)#Pushes computed value to the top of the stack
                
            elif value == "/": #Division
                calculatorStack.push(leftDigit / rightDigit)#Pushes computed value to the top of the stack
                
            elif value == "-": #Subtraction
                calculatorStack.push(leftDigit - rightDigit)#Pushes computed value to the top of the stack
                
    return calculatorStack.pop() #Clears the stack and returns the popped value

if __name__ == "__main__":
    print("Welcome to Postfix Calculator")
    print("Enter exit to quit")
    boolValue = False
    
    while not boolValue: #While True
        userExpression = input("Enter Expression \n")
        if userExpression == "exit":
            boolValue = True
            
        else:
            resultingStatement = postfix(userExpression) #Stores the popped value from the retiurn statement 
            print(f"Result: {resultingStatement}") #Formats output
    
    
                