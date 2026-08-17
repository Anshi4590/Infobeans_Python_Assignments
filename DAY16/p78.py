'''
123456789
 1+++++7
  1+++5
   1+3
    1
'''

n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
     for j in range (1,i):
         print(" ",end="")
     for k in range (1,(m*2-1)+1,+1):
         if k==1 or k==(m*2-1)or m*2==n*2: 
            print(k,end="")
         else:
            print("+",end ="")
     m-=1
     print()