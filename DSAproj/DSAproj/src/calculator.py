# _____________________________________________________________
# This program is a simple calculator that can process
# mathematical clauses given by a user. It supports some
# built-in functions along with the basic operations
# (addition, subtraction, division and multiplication), while
# also taking parentheses into account.
# _____________________________________________________________


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

# Prompting the user for a clause and turning it into a list
newclause = Clause(input("Give a clause: "))
splitClause = Clause.split(newclause)

# Shunting-yard algorithm for parsing the clause
# (implementation in progress)
while len(splitClause) >= 0:
    break