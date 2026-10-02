'''
*         *
 *      *
  *   *
    *
  *   *
 *      *
*         *

'''

n = int(input("Enter number:"))
i = 1
while i<=n:
      print()
      j = 1
      while j<=i:
          if j==i:
             print("*",end="")
          else:
            print(" ",end="")
          j+=1
      
      k=1
      while k<=2*(n-i)-1:
          print(" ",end="")
          k+=1
      m = 1
      while m<=i:
          if i==4 and m==1:
             print("",end="")
          elif m==1:
             print("*",end="")
          else:
            print(" ",end="")
          m+=1
      i+=1
      

i=1
a=i
while i<n:
    print()
    
    for j in range(1,n-i+1):
      if j==n-i+1-1:
          print("*",end="")
      else:
          print(" ",end="")

    k=1
   
    while k<=a:
        print(" ",end="")
        k+=1
    a+=2
    m = 1
    while m<=i:
        if i==4 and m==1:
            print("",end="")
        elif m==1:
            print("*",end="")
        else:
            print(" ",end="")
        m+=1
    i+=1
    







