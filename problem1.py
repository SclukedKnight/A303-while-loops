##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""
attempts = 3
tryable = True
while tryable == True:
    attempts = attempts - 1
    if attempts < 0:
        print("Access Denied, Too many failed attempts")
        tryable = False
    else:
        name = str(input("Please Enter Username: "))
        pswrd = str(input("Please Enter Password: "))

        if name == "admin" and pswrd == "12345":
            print("Access Granted")
            tryable = False
        else:
            print(f"Access denied, you have {attempts} many tries left")