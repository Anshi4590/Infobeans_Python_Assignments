'''
8.      *
       ***
      *****
     *******
    *********
'''

n = int(input("Enter number"))
i =1
while i<=n:
      print()
      j = n-i+1
      while j>=1:
           print(" " ,end ="")
           j-=1
      k=1
      
      while k<=i :
            print("*",end ="")
            k+=1
            
      
      l =1
      while l<i:
           print("*",end ="")
           l+=1
      i+=1


