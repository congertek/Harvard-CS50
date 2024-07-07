import os
import time

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen
clear_terminal()

name = input("What is your name? ")
print(f"Hello, {name}")