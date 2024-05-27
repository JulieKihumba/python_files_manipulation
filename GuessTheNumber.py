print("Welcome to the number guessing game!!")
print("I'm thinking of a number between 1 and 10.")
choice = int(input("what is that number?? "))

import random
numbers=[1,2,3,4,5,6,7,8,9,10]
my_choice = random.choice(numbers)

if choice == my_choice:

    print(f"I chose {my_choice}. So you got it right!!")
else:
    print(f"Sorry you did not get it right, i chose {my_choice} . Please try again next time")



    