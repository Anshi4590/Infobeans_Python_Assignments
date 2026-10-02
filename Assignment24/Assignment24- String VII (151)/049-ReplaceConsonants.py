''' 49.
Replace all consonants with '*' (Example suggests replacing non-vowels).
S = "apple" 
output: 
"ap*le" (or similar output depending on implementation)'''

s = input("Enter String")
m = ""
for i in s:
    if i.lower() not in "aeiou":
       i = "*"
       m+=i
    else:
        m+=i
print(m)

#using replace method

for  j in s:
    if j.lower() not in "aeiou":
        s = s.replace(j,"*")
print(s)
