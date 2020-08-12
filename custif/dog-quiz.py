#!/usr/bin/env python3

# greeting message
greeting = "So you've decided to get a dog, and it came down between a pitbull or a labrador retriever, let's see what fits you..."

# display greeting
print(greeting)


# main function
def main():
    pitbullScore = 0
    labScore = 0
    handler = "please enter yes or no"

    # question 1
    while True:
        q1 = input("Question 1: Do you want a dog that will scare people away?\n Enter yes or no: ")
        if q1 == "yes":
          pitbullScore += 1
          break
        elif q1 == "no":
          labScore += 1
          break
        else:
          print(handler)  
      

    # question 2
    while True:
        q2 = input("Question 2: The dog you want might not make a good watch dog. Is that ok?\n Enter yes or no: ")
        if q2 == "yes":
          labScore += 1
          break
        elif q2 == "no":
          pitbullScore += 1
          break
        else:
          print(handler)

    # question 3
    while True:
        q3 = input("Question 3: Do you have any small children at home?\n Enter yes or no: ")
        if q3 == "yes":
          labScore += 1
          break
        elif q3 == "no":
          pitbullScore += 1
          break
        else:
          print(handler)

    
    # deciding the winner
    if labScore > pitbullScore:
        print("looks like you should get a labrador! :)")
    else:
        print("pitbull seems like a good fit for you!")




main()

