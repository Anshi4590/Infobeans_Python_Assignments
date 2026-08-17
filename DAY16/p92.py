n=4

for i in range(1,n+1):
    print(" "*n,i,sep="")
for i in range(1,n+2):
    print(i,end="")
for i in range(n,0,-1):
    print(i,end="")
print()
for i in range(n,0,-1):
    print(" "*n,i,sep="")