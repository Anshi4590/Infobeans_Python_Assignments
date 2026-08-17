'''
11111
 2222
  333
   44
    5

'''
n = int(input("Enter number:"))
m = n
for i in range(1,n+1):
    for j in range(1,i):
       print(" ",end="")
    
    for k in range(1,m+1):
        print(i,end="")
        
    m-=1
    print()
