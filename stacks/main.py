"""
main interface for stacks
"""

from equations import equations as eq
from stack import Stack

import os
from random import randint


def game(qs: int) -> int:
    """The main game"""
    score = 0
    diff = 1
    answer_stack = Stack()

    while score < qs:
        num1, num2, op = eq.generate_question(diff)
        stringg = str(num1) + " " + op + " " + str(num2) + " = "
        u_ans = int(input(stringg))  # user answer
        c_ans = eq.answer(num1, num2, op)  # computer answer

        if u_ans == c_ans:
            score += 1
            answer_stack.push(u_ans)
            print("Correct! ", qs - score, " more needed!")

            if score % 5 == 0 and score < qs:
                diff += 1
                print("Ramping up difficulty...")
                print("Good luck!")

        else:
            print("You got that wrong! It was ", c_ans)

    print("Now that that's done, we have the real deal.")
    print("Type in your answers, once at a time, starting from your most recent answer!")
    print("If you ever get any wrong, skip to the next one!")

    _ = input("Click anything to start")

    curr = qs
    score = 0
    while not answer_stack.is_empty():
        current = answer_stack.pop()

        stmt = "Enter your answer for question number " + str(curr) + " "
        u_inp = int(input(stmt))

        if u_inp == current:
            score += 1
            print("Correct! Current score: ", score)

        else:
            print("Wrong! It was ", current)

        curr -= 1

    return score


def opening(p):
    """Opening lines"""
    print("Answer as many questions as you can!")
    print("Difficulty spikes up every so often. Try to keep up!")

    print("...")
    print("Oh, and for any division questions, round down any number you get! We just want the quotient")

    qs = int(input("To start, enter a target number: "))

    print("Great! You'll be asked question(s) until you get ", qs, " of them right. Keep track of your answers :)")
    if p == 0:
        print("You'll know why soon :D")

    return qs


if __name__ == "__main__":
    plays = 0
    while True:
        q = opening(plays)
        _ = input("Click anything to start")

        sc = game(q)
        print("That was the last one. Your final score: ", sc)
        replay = input("Try again? y/n: ")
        if replay == 'y':
            plays += 1
            os.system('cls')
        else:
            print("Good bye! ", eq.GOODBYES[randint(0, len(eq.GOODBYES) - 1)])
            break
