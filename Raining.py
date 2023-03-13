'''
Raining
Pawelski
3/13/2023
Python II

Instructions:
What do you need to enter to get the message
You better take an umbrella then."? What about the
message "No need for an umbrella."?

Modify the program so that it also asks if it is
sunny outside. If it is sunny, have the program
say the message "Protect your eyes, wear sunglasses.".

Modify the program by having the user enter boolean
values instead of strings.
'''

is_raining = input("Is it raining outside? (yes/no) >> ")
if is_raining == "yes":
    print("You better take an umbrella then.")
else:
    print("No need for an umbrella.")