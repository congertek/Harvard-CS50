import os

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen
clear_terminal()

#Get user input
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y, 3)

print(f"{z:,}")