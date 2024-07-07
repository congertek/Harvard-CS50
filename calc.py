import os

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen
clear_terminal()

#Get user input
x = int(input("What's x? "))
y = int(input("What's y? "))

#z = int(x) + int(y)

print(x + y)