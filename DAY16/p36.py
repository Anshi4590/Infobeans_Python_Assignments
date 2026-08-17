'''
ABCDE
A  D
A C
AB
A

'''
n = int(input("Enter number:"))

for i in range(n,0,-1):
    var = 65
    for j in range(1,i+1):
        if i==j or i==n or j==1:
           print(chr(var),end ="")
          
        else:
           print(" ",end ="")
        var+=1  
       
    print()
         
