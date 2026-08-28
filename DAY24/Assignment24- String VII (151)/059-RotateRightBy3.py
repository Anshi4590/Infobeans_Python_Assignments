'''59 Rotate characters right by 3 positions 
S = "abcde" 

"cdeab"'''

s = input("Enter String : ")
r = 3
new =""

for i in range(len(s)-r,len(s)):
    new+=s[i]

for j in range(len(s)-r):
    new+=s[j]

print(new)