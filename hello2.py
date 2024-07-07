import os

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen
clear_terminal()

# Define function hello
def hello(to):
    print("hello", to)


name = input("What is your name? ")
hello(name)
