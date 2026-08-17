'''
    1
   212
  32123
 4321234
543212345

'''
n = int(input("Enter number"))
i=1 
while i<=n:
      print()
      j=1
      while j<=n-i:
            print(" ",end="")
            j+=1
      k=i
      while k>=1:
            print(k,end="")
            k-=1
      else:
          k=2
          while k<=i:
            print(k,end="")
            k+=1  
      i+=1