'''
55555
4  4
3 3
22
1
'''

n =int(input("Enter number"))
for i in range(n,0,-1):
     for j in range(1,i+1):
          if i==j or i==n or j==1:
             print(i,end ="")
          
          else:
             print(" ",end ="")
          
       
     print()
