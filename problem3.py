#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""

num = {}
num[0] = 1
num[1] = 1
x = 2
go = True
while go == True:
    num[x] = num[x - 1] + num[x - 2]
    if num[x] > 100:
        go = False
    else:
        print(num[x])
        print("")
        x = x + 1