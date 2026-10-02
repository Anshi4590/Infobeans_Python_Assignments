'''
x
xx
xxx
xxxx
xxx
xx
x


'''

n =int(input("Enter number"))

for i in range(1,n):
    if i<=n:
        for j in range(0,i):
            print("*",end=" ")
        print()    
    
n1=n-1
m = n1
for i in range(1,n1+1):
    for j in range(1,m):
        print("*",end=" ")
    
    m-=1
    print()