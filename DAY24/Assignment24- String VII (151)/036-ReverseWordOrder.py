'''36.Reverse order of words. 
S = "one two three" 
Output :
"three two one"'''

s = input("Enter String : ")
m = s.split(" ")
result = ""
for i in range(len(m)-1,-1,-1):
    result+=m[i]+" "
print(f"Reverse order of words : {result}")