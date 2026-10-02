'''61 Count total alphabets, digits, and special characters. 
S = "a1b!c2" 
Alphabets: 3, 
Digits: 2, Special: 1'''

s = input("Enter String : ")

alphacount = 0
digitcount = 0
spacecount = 0
specialcount = 0

for i in s:

    if i.lower()>="a" and i.lower()<="b":
        alphacount+=1

    elif i>="0" and i<="9":
        digitcount+=1

    elif i == " ":
        spacecount+=1

    else:
        specialcount+=1

print(f"Alphabet  :{alphacount}")
print(f"Digit     :{digitcount}")
print(f"Special   :{specialcount}")
