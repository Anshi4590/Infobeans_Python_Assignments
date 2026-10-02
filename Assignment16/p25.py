'''
5
54
543
5432
54321
'''
n =int(input("Enter number : "))
i = 1

while i<=n:
      print()
      k = n
      j = 1
      while j<=i:
            print(k,end ="")
            k-=1
            j+=1
      i+=1 