'''
55555
 4__4
  3_3
   22
    1

'''


n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
    for j in range(1,i):
       print(" ",end="")
    for k in range(1,m+1):
       if k==1 or k==m or m==n:
          print(m,end="")
       else:
          print("_",end="")
    m-=1
    print()