# _____________________________________________________________
# This program is a simple calculator that can process
# mathematical clauses given by a user. It supports addition,
# subtraction, multiplication, division and powers, and also
# takes parentheses into account.
# _____________________________________________________________

from queue import Queue
from collections import deque

# Takes user input string and converts it into list of individual characters
def convert(string):    
    list=[]
    list[:0]=string
    return list

# Goes through the numbers in the list, and makes sure that the multi-digit numbers in the
# operation given by the user are registered as one element and not several different numbers

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
            i += 1
            raise Exception ("Input contains invalid symbols; accepted include (, ), /, *, +, -, ^")
    return readyList
    # Output is a list containing each element of theoperation given by the user

# Gives operator precedence for comparing operators in the shunting yard algorithm
def precedence (elem):
    if elem == "^":
        return 1
    if elem == "*" or elem == "/":
        return 2
    elif elem == "+" or elem == "-":
        return 3

# Checks whether operator is left-associative, used in
# comparing operators in the shunting yard algorithm
def associative (elem):
    if elem == "/" or elem == "-" or elem == "+" or elem == "*":
        return True

# Gets element on top of the stack
def peek (elem):
    return elem[-1]

# Shunting-yard algorithm for transforming the input clause
# (now transformed into a list) from infix into postfix form
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
    # Output is a queue where the elements are in postfix form


# Evaluating the postfix expression given by the shunting yard
# algorithm and solving the operation by doing the operations in
# the order determined by operator precedence and parentheses

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
    # Output is the result of the mathematical expression given by the user in the beginning

def main():
    expression = input("Give an operation: ")
    expression = separate(expression)
    expression = shuntingYard(expression)
    print("The result is " + str(postFixEval(expression)))

if __name__ == "__main__":
    main()