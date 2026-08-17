# write a program to print square ,cube and squareroot of all the number from 1 to n

import math
n = int(input("Enter the number"))
i = 1
while i<=n:
      square = i**2
      cube = i**3
      root = math.sqrt(i)
      print("Square of ", i,"=",square)
      print("Cube of ", i,"=",cube)
      print("Square root of ", i,"=",root)
      print()
      i =i+1
