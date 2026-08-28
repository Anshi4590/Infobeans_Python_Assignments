'''58 Rotate characters left by 2 positions. 
S = "abcde" 
output:

"cdeab"'''

s = input("Enter String : ")

first =""
rotate =""

for i in range(0,2):
    first+=s[i]
i=0
for j in range(i+2,len(s)):
    rotate+=s[j]

rotate+=first
print(rotate)
    
