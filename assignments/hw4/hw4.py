"""
Name: Richard Easley
hw4.py

Problem:  Use Python graphics utilizing author-supplied package
          Practice accumulating sequences

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to create new square.")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(70, 70))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to create squares
    for _ in range(num_clicks):
        click = win.getMouse()
        shape = Rectangle(Point(click.getX() - 10, click.getY() - 10),
                          Point(click.getX() + 10, click.getY() + 10))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)

    instructions.undraw()
    instructions = Text(inst_pt, "Click to quit")
    instructions.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    # Display information about rectangle drawn by user
    # Two mouse clicks for corners of rectangle
    # Draws rectangle and display perimeter and area of rectangle
    # Formulas used: area = length * width and perimeter = 2 * length + width

    win = GraphWin("Rectangle", 400, 400)

    inst_pt =  Point(400 / 2, 400 - 10)
    per_pt = Point(400 / 2, 400 - 30)
    instructions = Text(inst_pt, "Click two points to create rectangle")
    instructions.draw(win)

    pnt1 = win.getMouse()
    pnt2 = win.getMouse()
    shape = Rectangle(pnt1, pnt2)
    shape.setOutline("black")
    shape.setFill("green")
    shape.draw(win)

    length = abs(pnt1.getX() - pnt2.getX())
    width = abs(pnt1.getY() - pnt2.getY())
    area = length * width
    perimeter = (length * 2) + (width * 2)

    instructions.undraw()
    permtext = Text(per_pt, "Perimeter of rectangle is: " + str(perimeter))
    instructions = Text(inst_pt, "Area of rectangle is: " + str(area))
    instructions.draw(win)
    permtext.draw(win)

    win.getMouse()
    win.close()


def circle():
    # Click to set circle center
    # Click to set point on circle circumference
    # Display radius of circle
    # Instruct to end program

    win = GraphWin("Circle", 400, 400)

    rad_pt = Point(400 / 2, 400 - 30)
    inst_pt = Point(400 / 2, 400 - 10)
    instructions = Text(inst_pt, "Click two points to create circle.")
    instructions.draw(win)

    pnt1 = win.getMouse()
    pnt2 = win.getMouse()

    pnx1 = pnt1.getX()
    pnx2 = pnt2.getX()
    pny1 = pnt1.getY()
    pny2 = pnt2.getY()
    rad = math.sqrt(((pnx2 - pnx1)**2)+((pny2 - pny1)**2))

    shape = Circle(pnt1, rad)
    shape.setOutline("black")
    shape.setFill("blue")
    shape.draw(win)

    instructions.undraw()
    radius = Text(rad_pt, "Radius of circle is: " + str(rad))
    instructions = Text(inst_pt, "Click to end program.")
    instructions.draw(win)
    radius.draw(win)

    win.getMouse()


def pi2():
    numterms = eval(input("enter the number of terms to sum: "))
    acc = 0
    for i in range(numterms):
        num = 4
        den = 1 + (2*i)
        frac = (num / den) * ((-1)**i)
        acc = frac + acc
    print("pi approximation: ", acc)
    print("accuracy; ", math.pi - acc)


if __name__ == '__main__':
    squares()
    rectangle()
    circle()
    pi2()
