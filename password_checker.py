# Password Strength Checker

import re

#Password must be more than 7 characters, contains (digit, lowercase, uppercase, Special Character)


def strength_check(password):
    if len(password)<8:
        return "Weak : Length of password must be greater than 7"
    
    if not any(char.isdigit() for char in password):
        return "Weak : It must contain a digit"

    if not any(char.islower() for char in password):
        return "Weak : It must contain a lower case character"

    if not any(char.isupper() for char in password):
        return "Weak : It must contain a upper case letter character"
    
    if not re.search(r'[!@#$%^&*]', password) :
        return "Weak : You must enter a special character in your Password"
    
    return "Strong : Secure Password !"

def password_check():
    print("Welcome to Password Strength Check Program !")

    while True:
        ans=input("Enter Password (Press 'q' to exit program) : ")

        if ans.lower()=="q":
            break

        result=strength_check(ans)
        print(result)

if __name__=="__main__":
    password_check()
    