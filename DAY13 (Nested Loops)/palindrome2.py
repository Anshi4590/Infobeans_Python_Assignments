'''6.
Palindrome Number Range Checker

A barcode verification system checks for palindrome numbers within a specific range.
The user enters starting and ending numbers.
The system displays all palindrome numbers using nested loops.

Input:
Enter starting number: 100
Enter ending number: 200

Output:
Palindrome Numbers are:
101
111
121
131
141
151
161
171
181
191'''



k =int(input("Enter the number:")) 
l= int(input("Enter the number:"))

for i in range(k,l+1):
    temp =i
    rev = 0
    for j in range(len(str(i))):
        d = i%10
        rev = rev*10 + d
        i = i//10
    
    if  temp == rev:
        print(temp)
     