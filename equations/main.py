"""
main game interface
"""

import equations
import os
from random import randint

print("Answer as many questions as you can!")
print("Difficulty spikes up every so often. Try to keep up!")

print("...")
print("Oh, and for any division questions, round down any number you get! We just want the quotient")

_ = input("Click anything to start!")

score = 0
diff = 1

while True:
    num1, num2, op = equations.generate_question(diff)
    stringg = str(num1) + " " + op + " " + str(num2) + " = "
    u_ans = int(input(stringg))  # user answer
    c_ans = equations.answer(num1, num2, op)  # computer answer

    if u_ans == c_ans:
        score += 1
        print("Correct! Your score is now ", score)

        if score % 5 == 0:
            diff += 1
            print("Ramping up difficulty...")
            print("Good luck!")

    else:
        print("You got that wrong! It was ", c_ans)
        print("Your final score is ", score)

        replay = input("Try again? y/n: ")
        if replay == 'y':
            os.system('cls')

            score = 0
            diff = 1
            print("All values reset!")

        else:
            print("That was fun (I hope)!", equations.GOODBYES[randint(0, len(equations.GOODBYES)-1)])
            break
