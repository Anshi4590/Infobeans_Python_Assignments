'''
83 Create a string from a byte array. 

Byte[] = {72, 101, 108} 
(ASCII for H, e, l) "Hel"

'''
byte = list(map(int,input("Enter byte : ").split(" ")))
string = ""

for i in byte:
    string+=chr(i)

print(string)