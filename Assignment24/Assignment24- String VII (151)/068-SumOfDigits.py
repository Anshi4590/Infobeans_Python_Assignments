'''
68.Count the sum of digits present in a string. 
S = "a1b2c3" 6 (1+2+3)

'''

s = input("Enter String : ")
sum = 0

for i in range(0,len(s)):
    if s[i]>="0" and s[i]<="9":
        sum+=int(s[i])

print(f"The sum of digits present in a string : {sum}")
