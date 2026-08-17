'''
A B C D E
 A B C D
  A B C
   A B
    A

'''

n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
     for j in range (1,i):
         print(" ",end="")
     x = 65
     for k in range (1,m+1):
         print(chr(x),end=" ")
         x+=1
     m-=1
     print()