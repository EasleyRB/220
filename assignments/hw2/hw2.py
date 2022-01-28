"""
Name: Richard Easley
hw2.py

Problem: Develop simple Python programs that do input, produce output and do arithmetic.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper = eval(input("what is the upper bound? "))
    acc = 0
    for i in range(0, upper+1, 3):
        acc = acc + i
    print("sum of threes is", acc)


def multiplication_table():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i*j, end=" ")
        print()


def triangle_area():
    alpha = eval(input("Enter side a length: "))
    bravo = eval(input("Enter side b length: "))
    charlie = eval(input("Enter side c length: "))
    side = (alpha + bravo + charlie) / 2
    area = math.sqrt(side*(side-alpha)*(side-bravo)*(side-charlie))
    print("area is", area)


def sum_squares():
    lower = eval(input("Enter lower range: "))
    upper = eval(input("Enter upper range: "))
    acc = 0
    for i in range(lower, upper + 1):
        acc = acc + (i*i)
    print(acc)


def power():
    base = eval(input("Enter base: "))
    expo = eval(input("Enter exponent: "))
    acc = 1
    for _ in range(expo):
        acc = acc * base
    print(base, "^", expo, "=", acc)


if __name__ == '__main__':
    sum_of_threes()
    multiplication_table()
    triangle_area()
    sum_squares()
    power()
