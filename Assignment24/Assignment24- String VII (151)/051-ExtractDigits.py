'''51 Extract only digits. 
S = "a1b2c3" 
output -
"123" '''

# using method

s = input("Enter String : ")
result = ""
for i in s:
    if i.isdigit():
        result+=i

print(result)

# manually
num =""
for i in range(0,len(s)):

    if s[i]>="0" and s[i]<="9":
        num+=s[i]
        
print(num)
