#Rakshith Raghu (rr5de)
import random

number = int(input("What should the answer be?"))

if number == -1:
    answer = random.randint(1, 100)
else:
    answer = number

x = 1

while (x <= 5):
    choice = int(input("Guess a number:"))


    if(choice > answer):
        if(x == 5):
            print("You lose; the number was", answer)
            x=7
        else:
            print("The number is lower than that.")
            x=x+1
    elif(choice < answer):
        if(x==5):
            print("You lose; the number was", answer)
            x=7
        else:
            print("The number is higher than that.")
            x=x+1
    else:
        print("You win!")
        x= 7