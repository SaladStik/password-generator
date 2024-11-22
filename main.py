import os
import time
import string
import random

def genPass(passLength, includeUpper, includeLower, includeNumbers, includeSymbols):
    #* Generate password parameters
    characters = ""
    if includeUpper:
        characters += string.ascii_uppercase
    if includeLower:
        characters += string.ascii_lowercase
    if includeNumbers:
        characters += string.digits
    if includeSymbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected!"
    #* Generate password
    password = ''.join(random.choice(characters) for _ in range(passLength))
    return password

# ^ Main
def main():
    print(""" 
    █████████████████████████     ████████████████████      ███████████████    █████████████ ███████████████████████     
    ██   ███   ███    ██    ██     ███    ███   ███   ██    ██     ██    ████   ███    ██   ███   ██ ██ ██    ███   ██    
    ██████████████████████████  █  ███    █████████   ██    ██   ███████ ██ ██  ██████ █████████████ ██ ██    ███████     
    ██    ██   ██    ██    ███ ███ ███    ███   ███   ██    ██    ███    ██  ██ ███    ██   ███   ██ ██ ██    ███   ██    
    ██    ██   █████████████████ ███ ████████   ███████      ██████████████   ███████████   ███   ██ ██  ████████   ██    
                                                                                                                        
                                                                                                                        """)
    print("\n")
    # * Big text
    
    #* Get user settings
    passLength = int(input("Enter the length of the password: "))
    includeUpper = True if input("Include uppercase letters? (y/n): ").lower() == "y" else False
    includeLower = True if input("Include lowercase letters? (y/n): ").lower() == "y" else False
    includeNumbers = True if input("Include numbers? (y/n): ").lower() == "y" else False
    includeSymbols = True if input("Include symbols? (y/n): ").lower() == "y" else False
    print("\n\n\n")
    
    #* Generate password
    while True:
        password = genPass(passLength, includeUpper, includeLower, includeNumbers, includeSymbols)
        if password != "No character types selected!":
            print(f"Your password is: {password}")
        else:
            print("No character types selected!")
            break
        print("\n")
        choice = input("Do you want to generate another password?").lower()
        if choice == "n":
            with open("passwords.txt", "a") as file:
                file.write(f"{password}\n")
            print("Password saved to passwords.txt")
            break
        print("\n\n\n\n\n\n")

if __name__ == "__main__":
    main()