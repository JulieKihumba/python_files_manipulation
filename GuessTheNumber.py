print("Welcome to the number guessing game!!")
print("I'm thinking of a number between 1 and 10.")
choice = int(input("what is that number?? "))

import random
my_choice = random.randint(1,10)
guess_limit=3
score = 0

while guess_limit>1 and choice != my_choice:
    choice = int(input("Sorry you did not get it right. Guess again.What is that number?? "))
    guess_limit-=1
if choice == my_choice:
    if guess_limit==2:
        score=7
    elif guess_limit==1:
        score=5
    elif guess_limit==0:
        score =3
    
    print(f"Congratulations!!😁 I chose {my_choice} too.You got it right!!Your score is {score}")

else:
    score=0
    print(f"Sorry😞 you did not get it right, i chose {my_choice} . Please try again next time.Your score is {score}")



    