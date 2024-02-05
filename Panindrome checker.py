a=input("enter the vord/phrase/sequence to be reversed:")
b=a[::-1]   #starting reversal using slicing
if a == b:
    print(a,"is palindrome")
else:
    print(a,"is not palindrom")
