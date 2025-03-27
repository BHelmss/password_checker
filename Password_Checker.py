'''
Quick summary of the NIST password complexity recommendations from SP 800-63B:
Length: Minimum of 8 characters, support up to at least 64 characters. Longer passwords (e.g., 12+) are encouraged.

Complexity: No mandatory rules for specific character types (e.g., uppercase, numbers, special characters). Allow all printable ASCII and Unicode characters, including spaces.

Blacklists: Reject common, compromised, or predictable passwords (e.g., "password123", "qwerty"), including repetitive/sequential patterns.

Focus: Prioritize usability and length over forced complexity, encouraging memorable passphrases.
'''

'''
NEXT STEPS
1. Clean it up and make improve time complexity.
'''
import os
import argparse

#Define variables
feedback = []
common_words = []

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
rockyou_path = os.path.join(script_dir, 'rockyou.txt')

# Read the rockyou.txt file and store its contents in the common_words list
with open(rockyou_path, 'r', encoding='utf-8', errors='ignore') as file:
    common_words = file.read().splitlines()

#Function to check password length
def pwd_length(pwd):
    if len(pwd) < 8:
        feedback.append("Password too short, should be longer than 8 characters(12 or more recommended).")
        return feedback
    if len(pwd) >= 64:
        feedback.append("Password is too lengthy, NIST strandards encourage usability(less than 64 characters).")
        return feedback
    
#Check if password is in a common wordlist(rockyou.txt)
def check_commonpwds(pwd):
    if pwd in common_words:
            feedback.append("Password exists in a common password list, please select a different password.")
            return feedback

#Function to call upon other functions
def check_pwd(password):
    #Clear feedback for each password (Mode 2)
    feedback.clear()

    #Check password length
    pwd_length(password)

    #Check if password is in rockyou.txt
    check_commonpwds(password)
    
    #Print all feedback
    for i in feedback:
        print(i)

    #If no feedback tell that the password is strong.
    if len(feedback) == 0:
        print("The password is strong by NIST standards, no changes needed!!")

# Function to handle Mode 1 (Manual entry)
def mode_1():
    userInput = input("Please enter the password you want to check: ")
    print("\nCheck successful... feedback listed below!!\n")
    check_pwd(userInput)
    print()

#Function to handle Mode 2 (Importing password list)
def mode_2(wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as file:
            passwords = file.read().splitlines()
        print(f"\nChecking passwords from the wordlist: {wordlist_path}\n")
        for password in passwords:
            print(f"Checking password: {password}")
            check_pwd(password)
            print("-" * 50)
    except FileNotFoundError:
        print(f"Error: The file '{wordlist_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

#Define main
def main():
    parser=argparse.ArgumentParser(description="Password Compliance Checker")
    parser.add_argument(
        "-l", "--list",
        help="Path to a password list file to check line by line.",
        type=str
    )
    args=parser.parse_args()

    if args.list:
        #Mode 2: Use a wordlist
        mode_2(args.list)
    else:
        #Mode 1: Manual entry
        print("\nWelcome to the NIST 800-63B password compliance checker!!\n")
        mode_1()

if __name__ == "__main__":
    main()