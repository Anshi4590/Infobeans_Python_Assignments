'''35Find the first palindrome word.
 S = "this madam is here" 
 output
 "madam"'''

s = input("Enter String : ").lower()
m = s.split(" ")

for i in m:
    rev =""
    for j in range(len(i)-1,-1,-1):
        rev+=i[j]
        if rev == i :
            print(f"The first palindrome word is : {i}")
            break
        
