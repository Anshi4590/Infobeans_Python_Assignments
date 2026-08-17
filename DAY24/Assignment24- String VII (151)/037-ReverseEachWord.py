'''37. Reverse each word. 
S = "cat dog" 
output :
"tac god"
'''

n = input("Enter String : ")
m = n.split(" ")
rev = ""
for i in m:
    for j in range(len(i)-1,-1,-1):
            rev+=i[j]
    rev+=" "
print(f"Reverse each word:{rev}")