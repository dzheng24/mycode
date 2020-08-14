#!/usr/bin/env python3

# greeting message
greeting = "So you've decided to get a dog, and it came down between a pitbull or a labrador retriever, let's see what fits you..."

# display greeting
print(greeting)


# main function
def main():
    pitbullScore = 0
    labScore = 0
    isComplete = False
    handler = "please enter yes or no"


    while True:
      # question 1  
      q1 = input("Do you want a dog that will scare people away? Enter yes or no ")
      if q1 == "yes":
        pitbullScore += 1
        break
      elif q1 == "no":
        labScore += 1
        break
      elif q1 == "":
        print("You must answer the question.")
      else:
        print(handler)  
      

      # question 2
      q2 = input("Do you want a dog that will be loving to almost everyone? ")
      if q2 == "yes":
        labScore += 1
      elif q2 == "no":
        pitbullScore += 1
      else:
        print(handler)

      # question 3
      q3 = input("Your dog might not be the best guard dog, is that ok?  ")
      if q3 == "yes":
        labScore += 1
      elif q3 == "no":
        pitbullScore += 1
      else:
        print(handler)


    print("out of while loop")
main()

