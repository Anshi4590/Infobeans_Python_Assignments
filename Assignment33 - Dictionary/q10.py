'''10.

=========================================
EMAIL DOMAIN COUNTER
====================

emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]

Write a program to:

* Count users belonging to each email domain.

Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}

---'''

emails = list(input("Enter Departments : ").split())
print(emails)

d ={}

for i in emails:
    
    d[i] = d.get(i,0)+1

print(d)
