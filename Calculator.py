print("Welcome to this basic calculator program 🫠")
print("You can perform addition, subtraction, multiplication, and division on two numbers of your choice 🙂")
num1=input("Enter your first number: ")

operation=input("Please choose an operation: ( addition, subtraction, multiplication, and division )").lower()
num2=input("Enter your second number: ")
if operation == 'addition':
    print(f"{num1} + {num2} = {int(num1) + int(num2)}")
elif operation == 'subtraction':
    print(f"{num1} - {num2} = {int(num1) - int(num2)}")
elif operation == 'multilication':
    print(f"{num1} * {num2} = {int(num1) * int(num2)}")
elif operation == 'division':
    print(f"{num1} / {num2} = {int(num1) / (num2)}")    
else:
    print("Invalid operation. Please choose a valid operation.")