"""
Name: Richard Easley
hw1.py

Problem: Understand the editing and execution phases of a computer program.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)


def shooting_percentage():
    total = eval(input("Enter the player's total shots: "))
    shots = eval(input("Enter how many shots the player made: "))
    percent = (shots / total) * 100
    print("Shooting Percentage:", percent, "%")


def coffee():
    pounds = eval(input("How many pounds of coffee would you like? "))
    cost = 10.5
    shipping = 0.86
    total = pounds * (cost + shipping) + 1.5
    print("Your total is:", total)


def kilometers_to_miles():
    travel = eval(input("How many kilometers did you travel? "))
    miles = travel / 1.61
    print("That's", miles, "miles!")


if __name__ == '__main__':
    calc_rec_area()
    calc_volume()
    shooting_percentage()
    coffee()
    kilometers_to_miles()
