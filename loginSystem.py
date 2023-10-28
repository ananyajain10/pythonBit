print("CREATE YOUR ACCOUNT")
username = input("Enter username: ")
password = input("Enter password: ")

print("YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY!")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
user1= User(username,password) 

def Login():
    Your_username = input("Enter your username: ")
    Your_password = input("Enter your password: ")
    if Your_username == user1.username and Your_password == user1.password:
        print("Login successful!")
    else:
        print("Login failed!")

print("LOGIN TO YOUR ACCOUNT")
Login()