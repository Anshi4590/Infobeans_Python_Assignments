'''
1
10
1 1
1  0
10101

'''
n = int(input("Enter number : "))
i =1

while i<=n:
      print()
      j =1
      
      while j<=i:
           if i==j or j ==1 or i==n:
              if j%2==0:
                 print(0,end="")
              else:
                 print(1,end="")
           else:
              print(" ",end ="")
           j+=1
           
      i+=1
