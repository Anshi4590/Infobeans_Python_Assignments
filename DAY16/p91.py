'''
    1
    2
    3
    4
123454321
    4
    3
    2
    1

'''

n = int(input("Enter number"))
i=1 
while i<=n:
      print()
      j=1
      while j<=n-i:
            print(".",end="")
            j+=1
      k=1
      while k<=i:
            if k==i or i==n:
               print(k,end="")
               
            else:
               print(".",end="")
            k+=1
      i+=1

      
      