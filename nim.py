#Rakshith Raghu (rr5de)

print("The Game of Nim")
print("")

marbles = int(input("Number of marbles are in the pile:"))
first = input("Who will start? (p or c)").lower()

up = 0
round = 0
higher = ""
power = 0

x= 0
z= 0
while ( x < marbles):
    x = (2)**z
    z = z+1


while(marbles > 0):

    print("The pile has", marbles, "marbles in it.")
    round = marbles+1

    if(marbles > 1):
        up = int(marbles/2)
    else:
        up = 1


    if(first == "p"):
        higher = str(up)
      #  if(marbles > 1):
        while(round > up or round < 0):
            round = int(input("How many marbles do you want to take? (1-"+ higher + "):"))
        marbles = marbles - round
        first = "c"
       # else:
         #  while(round != 1):
          #     round = int(input("How many marbles do you want to take? (1-1):"))
         #  marbles = marbles - round
        #   first = "c"
    else:
        for i in range(z, -1, -1):
            power = (2**i)-1
            if(marbles == power):
                round = 1
                marbles = marbles -1
                break
            elif(power < marbles):
                round = marbles - power
                marbles = power
                break
        print("The computer takes", round, "marbles.")
        first = "p"


if(first == "c"):
    print("The computer wins!")
else:
    print("The player wins!")