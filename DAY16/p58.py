'''
ABCDE
 A__D
  A_C
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
       if k==1 or k==m or m==n:
          print(chr(l),end="")
       else:
          print("_",end="")
       l+=1
    m-=1
    print()
