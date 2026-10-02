'''30 Replace a word with another word. 
S = "old data", 
Old="old", 
New="new" 
ouput-
"new data"'''

n = input("Enter String : ")
old = input("Enter Old word  : ")
new = input("Enter New word  : ")
result = ""

for i in n.split(" "):
    if i == old :
       result+=new+" "
    else:
       result+=i+" "

print(result)
