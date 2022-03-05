"""
Name: Richard Easley
hw7.py

Problem: Writing functions
         Reading and writing text files

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""
import encryption


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    i = 1
    for line in in_file:
        new_line = line.split()
        for word in new_line:
            out_file.write(str(i) + " " + word + "\n")
            i += 1


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        # fix by multiplying new_line[2] by new_line[3]
        out_file.write(" ".join(new_line) + "\n")


def calc_check_sum(isbn):
    sum = 0
    ISBN = str(isbn)
    for i in range(len(ISBN)):
        num = int(ISBN[i]) * (10 - i)
        sum = sum + num
    return sum % 11


def send_message(file_name, friend_name):
    in_file = open(file_name, 'r')
    out_file = open(friend_name, 'w')
    for line in in_file:
        out_file.write(line + "\n")


def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, 'r')
    out_file = open(friend_name, 'w')
    for line in in_file:
        new_line = encryption.encode(line, key)
        out_file.write(new_line + "\n")


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file = open(file_name, 'r')
    out_file = open(friend_name, 'w')
    pad_file = open(pad_file_name, 'r')
    key = pad_file.read()
    print(key)
    for line in in_file:
        new_line = encryption.encode_better(line, key)
        out_file.write(new_line + "\n")


if __name__ == '__main__':
    number_words()
    hourly_wages()
    calc_check_sum()
    send_message()
    send_safe_message()
    send_uncrackable_message()
