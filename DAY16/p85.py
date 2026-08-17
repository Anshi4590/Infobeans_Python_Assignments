'''
   1
  12
 123
1234
 123
  12
   1

'''
n = int(input("Enter number:"))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    print()

for i in range(1,n):
    for j in range (1,i+1):
        print(" ",end="")
    for m in range(1,n-i+1):
        print(m,end="")
    print()



