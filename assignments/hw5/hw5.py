"""
Name: Richard Easley
hw5.py

Problem: Use Python strings and lists.
         Use Python indexing and slicing facilities

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    # Read a name in first then last order and display in last
    # then first separated by a comma.
    name = input("enter a name (first last): ")
    name = name.split(" ")
    first = name[0]
    last = name[1]
    print(last + ", " + first)


def company_name():
    # Input three-part domain name and print only company name
    dom = input("enter a domain: ")
    dom = dom.split(".")
    company = dom[1]
    print(company)


def initials():
    stu = eval(input("how many students are in the class? "))
    for i in range(stu):
        name = input("what is the name of student " + str(i+1) + "? ")
        name = name.split(" ")
        first = name[0]
        last = name[1]
        print(first[0] + last[0])


def names():
    namelist = input("enter a list of names: ")
    namelist = namelist.split(", ")
    for i in namelist:
        name = i.split(" ")
        init = name[0][0] + name[1][0]
        print(init, end=" ")


def thirds():
    num = eval(input("enter the number of sentences: "))
    letters = ""
    for i in range(num):
        sent = input("enter sentence " + str(i+1) + ": ")
        letters = letters + sent[0::3]
    print(letters)


def word_average():
    sent = input("enter a sentence: ")
    words = sent.split(" ")
    acc = 0
    for i in words:
        acc = acc + len(i)
    print(acc / len(words))


def pig_latin():
    sent = input("enter a sentence to convert to pig latin: ")
    sent = sent.lower()
    words = sent.split(" ")
    pig = ""
    for i in words:
        latin = i[1:] + i[0] + "ay"
        pig = pig + latin + " "
    pig = pig.rstrip()
    print(pig)


if __name__ == '__main__':
    # name_reverse()
    # company_name()
    # initials()
    # names()
    # thirds()
    # word_average()
    pig_latin()
