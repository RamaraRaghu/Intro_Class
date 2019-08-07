#Rakshith Raghu (rr5de)


entered= str(input("Give me 10 words!:").lower())
empty = entered.split()

x=0
while x == 0:
    if (entered.find(" ")> 0):
        word =  entered[:entered.find(" ")]
        entered = entered[entered.find(" ")+1:]
    else:
        word = entered
        x=1

    empty.append(word)


desiredlist = {1: empty[0],2: empty[1],3: empty[2],4: empty[3], 5: empty[4],6: empty[5],7: empty[6], 8: empty[7], 9: empty[8],10: empty[9]}
wordCount = str(input('Which word count do you want?:').lower())

x=0
y=1
while(y<=10):
    if(desiredlist[y]== wordCount):
        x = x+1
        y=y+1
    else:
        y=y+1


if(x == 0):
    print("The word '" + wordCount + "' appears no times.")
else:
    print("The word '" + wordCount + "' appears", x, "times.")