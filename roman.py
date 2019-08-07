#Rakshith Raghu (rr5de)

arabNumber = int(input("Enter an integer:"))
number_print = arabNumber
answer = ""

if(arabNumber > 0 and arabNumber < 4000):
    romanN = ["M", "CM", "D", "CD", "C", "XC", "L" , "XL", "X", "IX", "V", "IV", "I"]   #both lists have 13 values
    conN = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    x = 0
    for i in range(13):
        if(arabNumber >= conN[i]):
            z = int(arabNumber/conN[i])
            for z in range(0,z):
                answer = answer + romanN[i]
                arabNumber = arabNumber - conN[i]
        else:
            i=i
    print("In roman numerals,", number_print,  "is" , answer)

else:
    print("Input must be between 1 and 3999")
