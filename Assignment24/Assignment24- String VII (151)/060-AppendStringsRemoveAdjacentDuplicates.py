'''60 Append two strings but remove duplicate adjacent characters. 

S1 = "miss", 
S2 = "issippi" 

"misisipi"

'''

s1 = input("Enter String : ")
s2 = input("Enter String : ")
s = s1+s2
new =""

for i in range(0,len(s)):

    if s[i-1]!=s[i] or i==0:
        new+=s[i]
print(new)

# this is the second approch we can use

new = ""

for ch in s:
    if new == "" or ch != new[-1]:
        new += ch

print(new)

