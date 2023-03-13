'''
Change Colors
Pawelski
3/13/2023
Python II

Instructions:
Try entering "blue" for the color. What happens?
Try entering "red" or "green" for the color. What happens?
Do you think this is intentional?

Modify the program to use elif instea of else so that
the invalid message only appears when a color not listed
is entered. When should you use elif?
'''

import colorama

message = input("Enter a message >> ")
color = input("What color do you want the message to be? (red, green, blue) >> ")

if color == "red":
    print(colorama.Fore.RED + message)
if color == "green":
    print(colorama.Fore.GREEN + message)
if color == "blue":
    print(colorama.Fore.BLUE + message)
else:
    print("Invalid color! Defaulting to white.")
    print(colorama.Fore.WHITE + message)