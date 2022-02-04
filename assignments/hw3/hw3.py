"""
Name: Richard Easley
hw3.py

Problem: Develop simple Python programs that do input, produce output
and do arithmetic using loops. Develop simple Python programs that
use for loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    num = eval(input("how many grades will you enter? "))
    acc = 0
    for _ in range(num):
        grade = eval(input("Enter grade: "))
        acc = grade + acc
    avg = acc / num
    print("average is", float(avg))


def tip_jar():
    acc = 0
    for _ in range(5):
        tip = eval(input("how much would you like to donate? "))
        float(tip)
        acc = acc + tip
    print("total tips:", acc)


def newton():
    num = eval(input("What number do you want to square root? "))
    cycle = eval(input("How many times should we improve the approximation? "))
    approx = num
    for _ in range(cycle):
        approx = (approx+(num/approx))/2
    print("the square root is approximately", approx)


def sequence():
    terms = eval(input("how many terms would you like? "))
    for i in range(terms):
        print(1+((i//2)*2))


def pi():
    terms = eval(input("how many terms in the series? "))
    acc = 1
    for i in range(terms):
        num = 2 + ((i//2)*2)
        den = 1 + (((i+1)//2)*2)
        acc = acc * (num / den)
    print(acc * 2)


if __name__ == '__main__':
    average()
    tip_jar()
    newton()
    sequence()
    pi()
