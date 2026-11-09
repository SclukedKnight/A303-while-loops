#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
finish = False
while finish == False:
    x = int(input("Enter a number: "))
    if (x % 2) == 0:
        print(f"{x} is an even int :)")
        finish = True
    else:
        print(f"{x} is not an even intiger")