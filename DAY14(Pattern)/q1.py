# sum of of all the integer between 100 and 200 which are divisible by 9

n = int(input ("Enter the number"))
m = int(input("Enter the number"))
sum=0
for i in range ( n,m+1):
    if i%9==0:
       sum =sum+i
print(sum)
    