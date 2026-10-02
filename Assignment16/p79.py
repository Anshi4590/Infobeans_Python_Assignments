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
y=n
for i in range(1,2*n-1+1):
    if i<=n:
        for j in range(0,i):
            print("*",end=" ")
        print()
    
    if n-1<i:
        k=1
        for l in range(1,y):
            print("/",end=" ")
        print()
        k+=1

        y-=1
    
    
