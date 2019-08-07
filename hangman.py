#Rakshith Raghu(rr5de)

hangWord = str(input("Enter a word: ")).upper()
hangman = ""
hangmanTwo = ""
test_letter = ""

for z in range(len(hangWord)):
    hangman = hangman + "-"

i = 6
while(i > 0):
    test_letter = str(input("["+ hangman + "]" +" You have "+ str(i)+ " left, enter a letter:")).upper()

    if(test_letter in hangWord):
        length = len(hangman)
        hangmanTwo = hangman
        hangman = ""
        for z in range(length):
            if(test_letter == hangWord[z]):
                hangman = hangman + test_letter
            else:
                hangman = hangman + hangmanTwo[z]

        if("-" not in hangman):
            print("You win! The word was", '"'+hangWord+'"')
            i = 0
        else:
            print("Correct!")

    else:
        i = i-1
        if(i == 0):
            print("You lose! The word was", '"'+hangWord+'"')
        else:
            print("Incorrect!")

