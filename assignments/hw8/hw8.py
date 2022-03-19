"""
Name: Richard Easley
hw8.py

Problem: Utilize accumulations
         Use conditional control structures

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
from graphics import *


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc = acc + nums[i]
    return acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    acc = []
    for i in range(len(nums)):
        newnums = nums.split(",")
        to_numbers(newnums)
        square_each(newnums)
        nu_list = sum_list(newnums)
        acc.append(nu_list)
    return acc


def starter(weight, wins):
    if (weight >= 150 and weight < 160 and wins >= 5) or (weight > 199) or (wins > 20):
        return True
    return False


def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_b = win.getMouse()
    circumference_b = win.getMouse()
    radius_b = math.sqrt(
        (center_b.getX() - circumference_b.getX()) ** 2 + (center_b.getY() - circumference_b.getY()) ** 2)
    circle_two = Circle(center_b, radius_b)
    circle_two.setFill("red")
    circle_two.draw(win)
    over = Text(Point(5, 5), "The circles overlap.")
    n_over = Text(Point(5, 5), "The circles do not overlap.")

    if did_overlap(circle_one, circle_two):
        over.draw(win)
    else:
        n_over.draw(win)

    closetxt = Text(Point(5, 7), "Click to close.")
    closetxt.draw(win)
    win.getMouse()
    win.close()

    win.getMouse()


def did_overlap(circle_one, circle_two):
    radius1 = circle_one.getRadius()
    radius2 = circle_two.getRadius()
    center1 = circle_one.getCenter()
    c1x = center1.getX()
    c1y = center1.getY()
    center2 = circle_two.getCenter()
    c2x = center2.getX()
    c2y = center2.getY()

    cir_dis = math.sqrt(math.pow(c2x - c1x, 2) + math.pow(c2y - c1y, 2))
    add_rad = radius1 + radius2
    return cir_dis <= add_rad



if __name__ == '__main__':
    pass
