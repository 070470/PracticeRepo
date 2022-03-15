# _____________________________________________________________
# This program is a simple calculator that can process
# mathematical clauses given by a user. It supports some
# built-in functions along with the basic operations
# (addition, subtraction, division and multiplication), while
# also taking parentheses into account.
# _____________________________________________________________

from queue import Queue
from collections import deque
import unittest

"""
def tests():
    suite = unittest.TestLoader().loadTestsFromModule(test) 
    unittest.TextTestRunner(verbosity=2).run(suite)
"""

def convert(string):    # convert string into array
    list=[]
    list[:0]=string
    return list

def separate (clause):
    elemList = convert(clause)
    readyList = []
    i = 0
    opers = ["(", ")", "/", "*", "+", "-", "^"]
    while i < len(elemList):
        if elemList[i] in opers:
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
            raise Exception ("Input contains invalid symbols; accepted include (, ), /, *, +, -, ^")
            i += 1
    return readyList

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

# Get element on top of stack
def peek (elem):
    return elem[-1]

# Shunting-yard algorithm for transforming the clause from infix to postfix form
def shuntingYard (clause):
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
        elif token == "^":
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