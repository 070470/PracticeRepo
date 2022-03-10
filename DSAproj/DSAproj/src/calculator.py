# _____________________________________________________________
# This program is a simple calculator that can process
# mathematical clauses given by a user. It supports some
# built-in functions along with the basic operations
# (addition, subtraction, division and multiplication), while
# also taking parentheses into account.
# _____________________________________________________________

from queue import Empty, Queue
from typing import Deque
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

# Convert the input string into an array
def convert(string): 
    list1=[]
    list1[:0]=string
    return list1

# Create a new array where all elements are correctly separated (e.g. numbers with multiple digits
# are registered as one number and not separate elements)

def separate (clause): 
    elemList = convert(clause)
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
        elif elemList[i] == "s":
            readyList.append("sqrt")
            i += 4
        else:
            readyList.append(elemList[i])
            print(type(elemList[i]))
            i += 1
    return readyList

# Transform list into stack

def stackify (clause):
    clause.reverse()
    charStack = deque()
    for elem in clause:
        charStack.append(elem)
    return charStack

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
            print("alright")
            i += 1
        elif clause[i] != ("(" or ")"):
            print("okay")
            if len(operstack) > 1:
                while ((operstack[-1] != "(") and ((precedence(clause[i]) < precedence(operstack[-1]))
                    or ((precedence(clause[i]) == precedence(operstack[-1])) and associative(clause[i])))):
                    outputq.put(operstack.pop())
                    i += 1
                    print(i)
                operstack.append(clause[i])
        elif clause[i] == "(":
            print("hi")
            operstack.append(clause[i])
            i += 1
        elif clause[i] == ")":
            if len(operstack) > 1:
                while (operstack[-1] != ("(")):
                    assert len(operstack) > 0
                    outputq.put(operstack.pop())
                assert (operstack[-1] == "(")
                operstack.pop()
        else:
            print("ok")
        i += 1
    while (len(operstack) > 0):
        assert operstack[-1] != ("(" or ")")
        outputq.put(operstack.pop())
    print (outputq.queue)
    print(operstack)
    return outputq


# Evaluating the postfix expression / solving the operation
def postFixEval (queue):
    print(queue.queue)
    operstack = deque()
    while queue.qsize() > 0:
        token = queue.get()    # front?
        if isinstance(token, int):
            operstack.append(token)
        elif isinstance(token, character):
            if token == "+":
                b = operstack.pop()
                a = operstack.pop()
                operstack.append(a + b)
            if token == "-":
                b = operstack.pop()
                a = operstack.pop()
                operstack.append(a - b)
            if token == "*":
                b = operstack.pop()
                a = operstack.pop()
                operstack.append(a * b)
            if token == "/":
                b = operstack.pop()
                a = operstack.pop()
                operstack.append(a / b)
            if token == "^":
                b = operstack.pop()
                a = operstack.pop()
                operstack.append(a ^ b)
        return operstack.pop()

def main():
    expression = input("Give an operation: ")
    expression = separate(expression)
    expression = stackify(expression)
    expression = shuntingYard(expression)
    print(postFixEval(expression))

if __name__ == "__main__":
    main()