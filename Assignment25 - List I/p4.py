'''4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]'''

arr = list(map(int,input("Enter number:").split(" ")))
print(arr)
palindrome =[]
for i in arr:
    j = i
    rev = 0
    while j>0:
        digit = j%10
        rev = rev*10+digit 
        j = j//10
    
    if rev == i:
       palindrome.append(i)
print(palindrome)
if palindrome == []:
   print(f"Largest   : {-1}")
else:
   print(f"Largest     : {max(palindrome)}")
print(f"Count       : {len(palindrome)}")
print(f"Sorted      : {sorted(palindrome)}") 