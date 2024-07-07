import os
import time

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen
clear_terminal()
#Ask user for their name, Include Capitalize and Remove Whitespace
name = input("What is your name? ").strip().title()

#Split user's name into first and last
first, last = name.split(" ")

# Capitalize user's name
#name = name.strip().title()

# Remove whitespace from name
#name = name.title()

print(f"Hello, {first} {last}","|\n\n\n\n\n")