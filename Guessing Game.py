#Guessing Game
from random import randint
# guessnumber=int(input())
number=randint(1,100)
guess=int(input("enter the number:"))
while number!=guess:
    if guess<number:
        print("Too Low")
    elif guess>number:
        print("Too High")
    guess=int(input("enter the number:"))
else:
    print ("you guessed the correct number")
