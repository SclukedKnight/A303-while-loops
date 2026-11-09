#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
match = False
while not match == True:
    name = str(input("Enter Username: "))
    pswrd = str(input("Please enter pswrd: "))

    if name == "admin" and pswrd == "12345":
        print("access granted")
        match = True
    else:
        print("Access Denied")