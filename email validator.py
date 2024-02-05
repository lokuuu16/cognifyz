import re
#email validation using regular experessions i.e,regex
pattern_emailv=r'^[A-Za-z0-9.-_+%&*]+@[A-Za-z0-9.-]+\.[a-zA-Z]{2,5}$'

def validate(email):
    if(re.fullmatch(pattern_emailv,email)):
        print("the email address is valid")
    else:
        print("the email address is invalide")

email=input("Enter the email address to be validate:")
validate(email)
