#Rakshith Raghu(rrde)

code = str(input("Enter your cipher text:")).lower()

decoded = ""

regular = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",".",
           "!", "?", "0","1","2","3","4","5","6","7","8","9", " ","@","#","$","%","&",",","/",";",":","(",")"]
caesar = ["d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c",".",
           "!", "?", "0","1","2","3","4","5","6","7","8","9", " ","@","#","$","%","&",",","/",";",":","(",")"]

length = len(code)


for i in range(length):
    for z in range(0, 51):    #51
        if(code[i] == caesar[z]):
            decoded = decoded + regular[z]

        else:
            z=z
print("The decoded phrase is:", decoded)