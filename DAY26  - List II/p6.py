'''6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
'''

arr = list(map(int,input("enter element:").split(" ")))
print(arr)
prime =[]
for i in arr:
    flag =1
    if i<=1:
       continue
    
    else:
        for j in range(2,i):
            if i%j==0:
               flag = 0
               break
        if flag == 1:
            prime.append(i)
print(prime)
print(f"Sum : {sum(prime)}")
if prime == []:
    print("max",-1)
else:
    print(f"Max : {max(prime)}")
print(f"count : {len(prime)}")


'''arr = list(map(int, input("Enter numbers: ").split(",")))
prime=[]

for i in arr:
    if i<=1:
        continue
    else:
        j=2
        while j<=i:
            if i%j==0:
                break
            j+=1
        if j==i:
            prime.append(i)

print(f"Prime IDs : {prime}")
print(f"Sum       :{sum(prime)}")
print(f"Max       :{max(prime)}")
print(f"Count     :{len(prime)}")'''