# Implementation document

## Structure
The program consists of a single .py -file, and contains three core functionalities:

- A method for turning the input into a list where all elements (numbers and operators) are separated correctly
- The shunting yard algorithm implementation, which converts the input operation into postfix form
- The postfix stack evaluator function, which takes the postfix operation and makes the calculation to obtain the result of the operation.

The remaining smaller methods do things like converting the initial input string
into a list where all characters are separated, peeking the top element of a stack
or returning the precedence of an operator as a numerical value for comparison purposes.

## Time and space complexity
The program runs with a time and space complexity of O(n): both the shunting yard algorithm and
the postfix evaluator iterate through each element of the operation once, and both use a stack of
size n for storage during the program execution.

## Further improvements?
The program could be expanded to support built in functions, and variables like pi and e. Another
addition could be variables - the user could store the calculation results into variables, and
utilize the values of these variables in other calculations.

## Sources
- [Infix to postfix calculator] (https://www.free-online-calculator-use.com/infix-to-postfix-converter.html)
that I used to make sure my algorithm was coverting the expressions properly
- [Wikipedia] (https://en.wikipedia.org/wiki/Shunting-yard_algorithm) on the shunting yard algorithm
- Youtube on the [shunting yard algorithm] (https://www.youtube.com/watch?v=Wz85Hiwi5MY)
and [postfix evaluation] (https://youtu.be/bebqXO8H4eA) to help me grasp their idea
