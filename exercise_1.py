'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''


def get_numbers(start, end):
    return [x for x in range(start, end + 1) if x % 7 == 0 and x % 5 != 0]
