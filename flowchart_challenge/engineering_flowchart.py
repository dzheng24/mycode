#!/usr/bin/env python3

import sys

# function to quit program if user presses "q"
def handleQuit(input):
    if input == "q":
        print("Good bye")
        sys.exit(0)

# entrypoint
def main():
    print("Welcome to Engineering Flowchart. Press q at anytime to exit.\n\n")
    isMoving = input("Does it move?\n")
    handleIsMoving(isMoving)

# function that handles user's initial response  
def handleIsMoving(str):
    handleQuit(str)
    if str == "no":
        isShouldNotMoving = input("Should it?\n")
        handleShouldNotMoving(isShouldNotMoving)
    elif str == "yes":
        isShouldMoving = input("Should it?\n")
        handleShouldMoving(isShouldMoving)
    else:
        answer = input("Enter yes or no:\n ")
        handleIsMoving(answer)

# function that handles user's response when it is not supposed to move 
def handleShouldNotMoving(str):
    handleQuit(str)
    if str == "no":
        print("No problem")
    elif str == "yes":
        print("Try some WD-40")
    else: 
        answer = input("Enter yes or no:\n ")
        handleShouldNotMoving(answer)

# function that hanldes user's response when it is supposed to move 
def handleShouldMoving(str):
    handleQuit(str)
    if str == "yes":
        print("No problem")
    elif str == "no":
        print("Put some duct tape on it")
    else:
        answer = input("ENter yes or no:\n ")
        handleShouldMoving(answer)

main()

