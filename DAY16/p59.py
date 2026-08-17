'''
ABCDE
 ABCD
  ABC
   AB
    A

'''

n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
    for j in range(1,i):
       print(" ",end="")
    l = 65
    for k in range(1,m+1):
        print(chr(l),end="")
        l+=1
    m-=1
    print()
