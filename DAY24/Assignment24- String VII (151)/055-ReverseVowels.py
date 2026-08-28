'''55 Reverse only vowels. 
S = "hello" 
"holle"'''

s = input("Enter String:")

vowels =""
reverse =""
new =""

# first loop will extract vowels

for i in range(len(s)):
    if s[i] in "aeiou":
       vowels+=""+s[i]
print(vowels)

# second loop reverse the string in the vowels

for i in range(-1,-len(vowels)-1,-1):
    reverse+=vowels[i]
print(reverse)

j=0

# third loop will replace the vowels in string with string in reverse one by one

for i in range(len(s)):
    if s[i] in "aeiou":
        
        new+=reverse[j]
        j+=1
    else:
        new+=s[i]

print(new)





    
    