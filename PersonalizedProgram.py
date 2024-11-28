print("Welcome to our program 😁🫠")
print("We'll ask you some questions so that we can know you 🙂")
playing=input("Are you ready (Y/N)").lower()
if playing != "y":
    quit()
else:
    name=input("What is your name? ")
    favColor=input("What is your favourite color? ")
    print(f"Hello {name}! Your favourite color is {favColor}.")
