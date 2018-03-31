'''
https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
Question 9
Level 2

Question£º
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
'''

def solution_9(lines):
    return [line.upper() for line in lines]


def prints_solution(lines):
    solution = solution_9(lines)
    print(solution)
    return solution

