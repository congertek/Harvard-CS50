import os
import time

def clear_terminal():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

# Clear the screen
clear_terminal()
#Ask user for their name, Include Capitalize and Remove Whitespace
name = input("What is your name? ").strip().title()

# Capitalize user's name
#name = name.strip().title()

# Remove whitespace from name
#name = name.title()

print(f"Hello, {name}","|")