#write a program to print all the leap years between two years entered

n = int(input("Enter the number"))
m = int(input("Enter the number"))
print("The leap years are:")
for i in range (n,m+1):
    
    if i%4==0:
       print(i)
    else:
       continue

