
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack

def balance_parenthesis(a_string):
    opens = 0
    open_locations = []
    closes = 0

    stack1 = Stack()
    for i in a_string:
        stack1.push(i)


    index = 0
    while stack1.is_empty() == False:
        item = stack1.pop()
        if item == "(":
            opens += 1
            open_locations.append(index)
            index += 1
        elif item == ")":
            closes += 1
        


def main():
    print(balance_parenthesis("--(---(------)--"))
    print(balance_parenthesis("()----)"))
    print(balance_parenthesis("-----() -- ( () )"))
    print(balance_parenthesis("--(---(--(--(--())))--"))

if __name__ == "__main__":    main()