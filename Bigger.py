'''
Bigger
Pawelski
3/13/2023
Python II

Instructions:
Try a variety of number combinations to see what the program
prints. What numbers do you need to enter for all three messages
to appear? Why does this happen?

Modify the program so only one message will appear each time
the program runs. How did you accomplish this? What is the
difference between >= and >?
'''

number1 = int(input("Enter a number >> "))
number2 = int(input("Enter another number >> "))
if number1 >= number2:
    print(str(number1) + " is the bigger number.")
if number1 <= number2:
    print(number2, "is the bigger number.")
if number1 == number2:
    print("The numbers are the same.")