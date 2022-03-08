# _____________________________________________________________
# This program is a simple calculator that can process
# mathematical clauses given by a user. It supports some
# built-in functions along with the basic operations
# (addition, subtraction, division and multiplication), while
# also taking parentheses into account.
# _____________________________________________________________

from queue import Queue
from numpy import character
from torch import Stack

# Creating the structure and the functions for the clause
# (in progress)
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

# Prompting the user for a clause and turning it into a list
newClause = Clause(input("Give a clause: "))
splitClause = Clause.split(newClause).reverse()
charStack = Stack()
for elem in splitClause:
    charStack.append(elem)

def precedence (elem):
    if elem == "^":
        return 1
    if elem == "*" or elem == "/":
        return 2
    elif elem == "+" or elem == "-":
        return 3

def associative (elem):
    if elem == "/" or elem == "-":
        return True

def peek (elem):
    return elem[-1]

# Shunting-yard algorithm for parsing the clause
# (implementation in progress)

def shuntingYard (list):
    # Creating the output queue and operator stack for the 
    outputq = Queue()
    operstack = Stack()
    while Clause.length(splitClause) >= 0:
        token = splitClause[1]
        if isinstance(token, float):
            outputq.put(token)
        elif isinstance(token, function):
            operstack.append(token)
        elif isinstance(token, character) and token != ("(" or ")"):
            elem = operstack[-1]
            while ((elem != "(") and ((precedence(token) < precedence(elem))
                or ((precedence(token) == precedence(elem)) and associative(token)))):
                outputq.append(operstack.pop())
            operstack.append(token)
        elif token == "(":
            operstack.append(token)
        elif token == ")":
            while (peek(operstack) != ("(")):
                assert len(operstack) > 0
                outputq.append(operstack.pop())


        break

    # postFixStackEvaluator