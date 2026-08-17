'''4.
Armstrong Number Finder

A digital number analysis system checks for Armstrong numbers within a range.
The user enters starting and ending numbers.
The system finds all Armstrong numbers using nested loops.

Input:
Enter starting number: 1
Enter ending number: 500

Output:
Armstrong Numbers are:
1
153
370
371
407'''


n = int(input("Enter starting number: "))
m = int(input("Enter ending number: "))

for i in range(n, m + 1):
    temp = i
    copy = i
    l = len(str(i))
    sum = 0

    while copy > 0:
        d = copy % 10
        sum = sum + d ** l
        copy = copy // 10

    if temp == sum:
        print(temp)   
