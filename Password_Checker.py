'''
Quick summary of the NIST password complexity recommendations from SP 800-63B:
Length: Minimum of 8 characters, support up to at least 64 characters. Longer passwords (e.g., 12+) are encouraged.

Complexity: No mandatory rules for specific character types (e.g., uppercase, numbers, special characters). Allow all printable ASCII and Unicode characters, including spaces.

Blacklists: Reject common, compromised, or predictable passwords (e.g., "password123", "qwerty"), including repetitive/sequential patterns.

Focus: Prioritize usability and length over forced complexity, encouraging memorable passphrases.
'''

'''
NEXT STEPS (Delete this after done.)

1. Incorporate rockyou.txt instead of hardcoded wordlist

2. Figure out how to set different modes. One for manual entry, like is currently set and one for inputting a password list 
that will go through each password line by line. 

3. Clean it up and make improve time complexity.

'''
#Define variables
feedback = []
common_words = ['password', 'qwerty', '123456789']

#Have user select between mode 1 or mode 2
#Mode 1 is to maunally enter a password and Mode 2 is to enter a list of passwords

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
    for i in common_words:
        if pwd == i:
            feedback.append("Password exists in a common password list, please select a different password.")
            return feedback

#Function to call upon other functions
def check_pwd(password):

    #Check password length
    pwd_length(password)

    #Check if password is in rockyou.txt
    check_commonpwds(password)
    
    #Print all feedback
    for i in feedback:
        if i is not "None":
            print(i)

    #If no feedback tell that the password is strong.
    if len(feedback) is 0:
        print("The password is strong by NIST standards, no changes needed!!")


#Define main
def main():
    print("\nWelcome to the NIST 800-63B password compliance checker!!\n")
    userInput = input("Please enter the password you want to check: ")

    #Use the userInput as parameter for the check_pwd function
    print("\nCheck successful... feedback listed below!!\n")
    check_pwd(userInput)
    print()
main()