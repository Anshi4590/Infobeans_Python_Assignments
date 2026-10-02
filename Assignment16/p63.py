'''
    A
   A B
  A B C
 A B C D
A B C D E 
 
'''

n = int(input("Enter number:"))
for i in range(1,n+1):
     for j in range (0,n-i):
         print(" ",end="")
     m = 65
     for k in range (1,i+1):
         print(chr(m),end=" ")
         m+=1
     print()
