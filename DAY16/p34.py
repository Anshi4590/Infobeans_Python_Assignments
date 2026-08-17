'''
EEEEE
DDDD
CCC
BB
A
'''
n = int(input("Enter number :"))
var = 65+n-1
for i in range (0,n+1):
     for j in range (n,0,-1):
         print(chr(var),end ="")
     var-=1
     n-=1
     print()