""" Get as many problems correct (in a row)!
"""

import random

SYMBOLS = '+-*/'
GOODBYES = ["Don't procrastinate!",
            "Stay safe!",
            "Good luck on anything really!",
            "Have fun doing whatever",
            ":D:D:D:D:D:D"]


def generate_question(difficulty: int) -> (int, int, str):
    """ generate equations involving 2 random numbers of unknown digits

    :param difficulty: minimum of 1 and progressively gets higher
    :return: num1, num2, operator (op) (e.g. 1*2 where 1 is num1, 2 is num2, * as operator)

    - difficulty defines the number of digits for num1, num2
    """
    max_limit = difficulty*15  # numbers generated will range between 1, limit (for difficulties 1 - 3)
    min_limit = max(1, max_limit - 45)

    num1 = random.randint(min_limit, max_limit)
    num2 = random.randint(min_limit, max_limit)

    symb = random.randint(0, 3)
    op = SYMBOLS[symb]

    return num1, num2, op


def answer(num1: int, num2: int, op: str) -> int:
    """ checks user input answer

    :param num1: first number in equation
    :param num2: second number in equation
    :param op: third numebr in equation
    :return: answer

    - note that only quotient (in integers) are required for division questions
    """
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        return num1 // num2



