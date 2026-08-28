'''53 Remove all punctuation characters. 
S = "Hello, world!" 
output:
"Hello world"'''

s = input("Enter String : ")
new =""

for i in s:
    if i.isalnum() or i in" _":
        new +=i

print(new)