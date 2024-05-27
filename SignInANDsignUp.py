print("Create your account")
username=input("Enter Username: ")
password=input("Enter Password: ")
print("User 'admin' created sucessfully")
print("Login Now")

username2=input("Enter Username: ")
password2=input("Enter Password: ")
if username2==username and password2==password:
    print("Login Sucessful")
else:
    print("Invalid Credentials")