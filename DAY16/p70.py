'''
    A
   B B
  C   C
 D     D
EEEEEEEEE

'''


n = int(input("Enter number"))
for i in range(1,n+1):
    for j in range(0,n-i):
        print(" " ,end="")
    m = 65
    for k in range(1,(i*2-1)+1):
        if k==1 or i==n or k==i*2-1:
           print(chr(m),end="")
        else:
           print(" ",end="")
    m+=1
    print()