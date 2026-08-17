'''

123456
54321
1234
321
12
1

'''

n = int(input("Enter number:"))
for i in range(n,0,-1):
    if i%2==0:
       for j in range(1,n+1):
           print(j,end="")
           
    else:
       for j in range(n,0,-1):
           print(j,end="")
    n-=1
    print()