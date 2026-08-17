'''23 Print all characters that occur exactly twice. S = "aabbcdee" 
 output = b', 'e' '''
s = input("Enter String : ")
result = ""
for i in s:
    count = 0
    if i not in result:
        for j in s:
            if i == j:
               count+=1
        if count == 2:
            result+=i
print(result)
