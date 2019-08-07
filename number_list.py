#Rakshith Raghu (rr5de)

list = []

a = int(input("Number 1:"))
b = int(input("Number 2:"))
c = int(input("Number 3:"))
d = int(input("Number 4:"))
e = int(input("Number 5:"))

list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)

aver = float(sum(list)/5)
rang = int(max(list)-min(list))

print("")
print("You entered:", list)
print("The average is:", aver)
print("The range is:", rang)

f = int(input("Which item do you want to remove?"))
list.remove(f)   #found syntax at https://docs.python.org/2/tutorial/datastructures.html

print("")
print("The new list has the following values:", list)
aver = float(sum(list)/4)
rang = int(max(list)-min(list))
print("The average is:", aver)
print("The range is:", rang)
