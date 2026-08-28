'''65 Count palindromic substrings. 

S = "aaa"

6 (a, a, a, aa, aa, aaa)

'''


s = input("Enter String : ")
count = 0

for i in range(len(s)):

    new =""
    print(s[i])
    new+=s[i]

    for j in range(i+1,len(s)):
        new+=s[j]
        rev=""
        for i in range(-1,-len(new),-1):
            rev+=new[i]
        if new == rev:
            count+=1  
            print(new)

print(f"The total count of the Palindrome Substring : {count}")