'''n = int(input("Enter number"))
square= n**2
rev=0
for i in range(len(str(n))):
    d = square%10
    rev = rev*10 +d
    square = square//10
print(rev)
new =0
for j in range(len(str(rev))):
    d1= rev%10
    new = new*10 +d1
    rev = rev//10
print(new)

if n == new:
   print("Automorphic number")
else:
   print("not a Automorphic number")'''



n = int(input("enter number"))
while n>0:
  d = n%10
  if d == 0:
     print("duck number")
     break
n = n//10
else:
   print("not a duck  number")

