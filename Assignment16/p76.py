'''
5 5 5 5 5
 4 4 4 4
  3 3 3
   2 2
    1

'''
n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
     for j in range (1,i):
         print(" ",end="")
     for k in range (1,m+1):
         print(m,end=" ")
     m-=1
     print()