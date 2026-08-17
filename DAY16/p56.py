'''
12345
 1__4
  1_3
   12
    1

'''

n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
    for j in range(1,i):
       print(" ",end="")
    for k in range(1,m+1):
       if k==1 or k==m or m==n:
          print(k,end="")
       else:
          print("_",end="")
    m-=1
    print()