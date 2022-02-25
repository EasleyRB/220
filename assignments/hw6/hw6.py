"""
Name: Richard Easley
hw6.py

Problem: Work with strings
         Writing functions that accept arguments and return values
         Modifying an object in a parameter

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Faith Kelley
"""
import math


def cash_converter():
    value = eval(input("enter an integer: "))
    print("$"+'{:.2f}'.format(value))


def encode():
    mess = input("enter a message: ")
    key = eval(input("enter a key: "))
    acc = ""
    for i in mess:
        och = ord(i)
        shift = och + key
        nch = chr(shift)
        acc = acc + nch
    print(acc)


def sphere_area(radius):
    sphar = 4 * math.pi * (radius**2)
    return sphar


def sphere_volume(radius):
    sphvo = (4 / 3) * math.pi * (radius**3)
    return sphvo


def sum_n(number):
    acc = 0
    for i in range(number + 1):
        acc = acc + i
    return acc


def sum_n_cubes(number):
    acc = 0
    for i in range(number + 1):
        acc = acc + (i**3)
    return acc


def encode_better():
    pltxt = input("enter a message: ")
    cypherwd = input("enter a key: ")
    acc = ""
    for i in range(len(pltxt)):
        charnum = (ord(pltxt[i])) - 65
        key = (ord(cypherwd[i % len(cypherwd)])) - 65
        shift = (charnum + key) % 58
        shift_2 = shift + 65
        newcha = chr(shift_2)
        acc = acc + newcha
    print(acc)

# should output JWVVPST with inputs: dolphin, ace


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    encode_better()
