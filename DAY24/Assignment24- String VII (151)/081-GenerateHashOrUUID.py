'''
81.Generate a hash code or UUID. 
S = "test" Hash: 3556498 (Example hash code)

'''

s = input("Enter String : ")

hash = 0

for i in s:

    hash = hash*31 + ord(i)

print(f"The Hash value of the '{s}' : {hash}")