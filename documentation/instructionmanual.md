# Instruction manual

## Running the program
Download the program release as either a zip or a tar file according to your preference, and
extract it to your desired location. Then navigate to the source folder of the program (i.e. _src_) in your terminal, and run the command
> python3 calculator.py

The program asks the user for an operation, which you can write into the terminal.
The program accepts inputs containing the following symbols: ()/+*-^ , and any numbers, and so the user
can give any mathematical expression containing the above symbols for the program to solve. After evaluating
the expression, the program gives the solution of the operation as an output into the terminal.

## Running tests
The tests can be run in the same source folder with the command
> coverage run --branch -m unittest testCalculator
A coverage report can be created with the command
> coverage html
