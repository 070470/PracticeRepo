# _____________________________________________________________
# This program is a simple calculator that can process
# mathematical clauses given by a user. It supports some
# built-in functions along with the basic operations
# (addition, subtraction, division and multiplication), while
# also taking parentheses into account.
# _____________________________________________________________

from queue import Empty, Queue
from numpy import character
from collections import deque

"""
# Creating the structure and the functions for the clause
class Clause:   
    def __init__(self, inputClause):
        self.inputClause = inputClause

    def printResult(self):
        print ("")

    # Turning the clause from a string into a list of characters
    def split(self):
        return list(self.inputClause)

    def length(self):
        return len(self.items)
"""

def Convert(string):    #convert string into array
    list1=[]
    list1[:0]=string
    return list1

def separate (clause):
    elemList = Convert(clause)
    readyList = []
    i = 0
    while i < len(elemList):
        if elemList[i] == ("("  or ")" or "/" or "*" or "+" or "-" or "^"):
            readyList.append(elemList[i])
            i += 1
        elif elemList[i].isnumeric():
            numbers = ""
            while i < len(elemList) and elemList[i].isnumeric():
                numbers = numbers + elemList[i]
                i+=1
            readyList.append(int(numbers))
            numbers = ""
        else:
            readyList.append(elemList[i])
            i += 1
    return readyList

# Transform list into stack
"""
def stackify (clause):
    clause.reverse()
    charStack = deque()
    for elem in clause:
        charStack.append(elem)
    return charStack
"""

# Set operator precedence
def precedence (elem):
    if elem == "^":
        return 1
    if elem == "*" or elem == "/":
        return 2
    elif elem == "+" or elem == "-":
        return 3

# Check whether operator is left-associative
def associative (elem):
    if elem == "/" or elem == "-" or elem == "+" or elem == "*":
        return True

def peek (elem):
    return elem[-1]

# Shunting-yard algorithm for transforming the clause from infix to postfix form
def shuntingYard (clause):
    # Creating the output queue and operator stack
    outputq = Queue()
    operstack = deque()
    i = 0
    while i < len(clause):
        if isinstance(clause[i], float) or isinstance (clause[i], int):
            outputq.put(clause[i])
        elif clause[i] != "(" and  clause[i] != ")":
            while len(operstack) > 0 and (peek(operstack) != "(" and ((precedence(clause[i]) > precedence(peek(operstack)))
                or ((precedence(clause[i]) == precedence(peek(operstack))) and associative(clause[i])))):
                outputq.put(operstack.pop())
            operstack.append(clause[i])
        elif clause[i] == "(":
            operstack.append(clause[i])
        elif clause[i] == ")":
            if len(operstack) > 0:
                while (peek(operstack) != "("):
                    assert len(operstack) > 0
                    outputq.put(operstack.pop())
                assert peek(operstack) == "("
                operstack.pop()
        i += 1
    while (len(operstack) > 0):
        assert peek(operstack) != "(" and peek(operstack) != ")"
        outputq.put(operstack.pop())
    return outputq

# Evaluating the postfix expression / solving the operation
def postFixEval (queue):
    operators = deque()
    q = list(queue.queue)
    for token in q:
        if isinstance(token, int):
            operators.append(token)
        elif token == "+":
            b = operators.pop()
            a = operators.pop()
            operators.append(a + b)
        elif token == "-":
            b = operators.pop()
            a = operators.pop()
            operators.append(a - b)
        elif token == "*":
            b = operators.pop()
            a = operators.pop()
            operators.append(a * b)
        elif token == "/":
            b = operators.pop()
            a = operators.pop()
            operators.append(a / b)
        else:
            b = operators.pop()
            a = operators.pop()
            operators.append(a**b)
    return operators.pop()

def main():
    expression = input("Give an operation: ")
    expression = separate(expression)
    expression = shuntingYard(expression)
    print("The result is " + str(postFixEval(expression)))

if __name__ == "__main__":
    main()