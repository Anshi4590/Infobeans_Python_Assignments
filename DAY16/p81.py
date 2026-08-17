'''
1
1 2
1  3
1   4
1  3
1 2
1

'''

n =int(input("Enter number"))

for i in range(1,n):
    if i<=n:
        for j in range(1,i+1):
            if j==1 or j==i:
               print(j,end=" ")
            else:
               print(" ",end=" ")
        print()    
    
n1=n-1
m = n1
for i in range(1,n1+1):
    for j in range(1,m):
       if j==1 or j==m-1:
          print(j,end=" ")
       else:
          print(" ",end=" ")
    
    m-=1
    print()
