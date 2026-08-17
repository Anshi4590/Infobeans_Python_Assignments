'''
54321
5432
543
54
5

'''

n = int(input("Enter number:"))
for i in range (0,n+1):
    for j in range (n,i,-1):
        print(j,end="")
    print()