'''50 Remove all digits. 
S = "a1b2c3"
"abc" '''

s = input("Enter String : ")
result =""

for i in range(0,len(s)):

    if s[i]>="0" and s[i]<="9":
       continue
    else:
        result+=s[i]
        
print(s)
