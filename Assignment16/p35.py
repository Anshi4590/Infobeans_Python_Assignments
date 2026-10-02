'''
*****
*  *
* *
**
*

'''

n = int(input("Enter number:"))

for i in range (n,0,-1):
    for j in range(1,i+1):
        if i==j or i==n or j==1:
           print("*",end ="")
        else:
           print(" ",end ="")
   
    print()
    print