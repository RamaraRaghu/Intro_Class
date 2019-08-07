#Rakshith Raghu (rr5de)

card = str(input("Type a credit card number (just digits):"))


odds = 0
evens = 0
length = len(card)
if(length%2 != 0):
    for i in range(0, length-1,2):
            evens = evens + int(card[i])
    for i in range(1, length-1, 2):
            odds = odds + ((2*int(card[i]))//10) + ((2*int(card[i]))%10)
else:
    for i in range(length-1,0,-2):
         evens = evens + int(card[i])
    for i in range(0, length-1, 2):
        odds = odds + ((2*int(card[i]))//10) + ((2*int(card[i]))%10)

answer = (evens + odds)%10
if(answer == 0):
    print("Yes,", card, "is a valid credit card number")
else:
    print(card, "is not a valid credit card number")