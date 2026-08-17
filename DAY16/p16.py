'''
a
bc
def
ghij
klmno

'''
 
n = int(input("Enter number : "))
i = 1
k = 97
while i<=n:
      print()
      j =1
      while j<=i:
            print(chr(k),end="")
            k+=1
            j+=1
      i+=1
      