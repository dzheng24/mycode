#!/usr/bin/env python3

"""
Engineering Flowchart Practice Using Python Functions
"""
import sys

MESSAGE = "Enter yes or no:\n"


def handle_quit(string):
    """exit the program if input is q"""
    if string == "q":
        print("Good bye")
        sys.exit(0)


def main():
    """calling the is_moving function based on user input"""
    print("Welcome to Engineering Flowchart. Press q at anytime to exit.\n\n")
    is_moving = input("Does it move?\n")
    handle_is_moving(is_moving)


def handle_is_moving(string):
    """function that handles user's initial response"""
    handle_quit(string)
    if string == "no":
        is_should_not_moving = input("Should it?\n")
        handle_should_not_moving(is_should_not_moving)
    elif string == "yes":
        is_should_moving = input("Should it?\n")
        handle_should_moving(is_should_moving)
    else:
        answer = input(MESSAGE)
        handle_is_moving(answer)


def handle_should_not_moving(string):
    """function that handles user's response when it is not supposed to move"""
    handle_quit(string)
    if string == "no":
        print("No problem")
    elif string == "yes":
        print("Try some WD-40")
    else:
        answer = input(MESSAGE)
        handle_should_not_moving(answer)


def handle_should_moving(string):
    """function that handles user's response when it is supposed to move"""
    handle_quit(string)
    if string == "yes":
        print("No problem")
    elif string == "no":
        print("Put some duct tape on it")
    else:
        answer = input(MESSAGE)
        handle_should_moving(answer)


main()
