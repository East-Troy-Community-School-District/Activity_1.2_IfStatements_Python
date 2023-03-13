'''
Staff Directory
Pawelski
3/13/2023
Python II

Instructions:
What is the difference between the logical operator
and and the logical operator or?

Modify the program by adding yourself to the staff
directory. People should be able to search for
you by last name or initals.
'''

name = input("Enter the name of the person you want to search for >> ")

if name == "Pawelski" or name == "NP":
    print("Nolan Pawelski - Comp Sci Teacher")
    print("262-642-6760 x5250")
elif name == "Hoff" or name == "MH":
    print("Michael Hoff - Tech Ed Teacher")
    print("262-642-6760 x5233")