'''5. Palindrome Check
A number plate is considered special if it reads the same forward and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a palindrome using loops*.

Input: 121
Output: Palindrome'''






n = int(input("Enter the number:"))
# rev = ""
temp = n

'''for i in n:
      rev = i +rev'''

reverse = 0
while n>0:
    d = n%10
    reverse = reverse*10 + d
    n = n//10
print(reverse)

if reverse == temp:
    print("palindrome")
else:
    print("not a palindrome")   