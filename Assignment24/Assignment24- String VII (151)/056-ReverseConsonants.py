'''56 Reverse only consonants.
 S = "apple" 
 "eplpa"'''

s = input("Enter String:")

consonent =""
reverse =""
new =""

# first loop will extract consonent

for i in range(len(s)):
    if s[i] not  in "aeiou":
      consonent+=""+s[i]
print(consonent)

# second loop reverse the string in the consonent

for i in range(-1,-len(consonent)-1,-1):
    reverse+=consonent[i]
print(reverse)

j=0

# third loop will replace the consonent in string with string in reverse one by one

for i in range(len(s)):
    if s[i] not in "aeiou":
        
        new+=reverse[j]
        j+=1
    else:
        new+=s[i]

print(new)