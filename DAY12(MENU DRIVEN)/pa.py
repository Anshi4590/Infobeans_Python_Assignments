a = int(input("enter num"))
b = int(input("enter num"))
sum =0
for i in range(a,b+1):
   for j in range(1,i//2+1):
        if i%j ==0:
           sum = sum +j
        print(sum)
   if sum == i:
     print(i)
   