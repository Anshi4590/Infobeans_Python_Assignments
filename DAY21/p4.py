
'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d

'''
n = input("Enter String:")
maxcount = 0
maxchar =""
for i in range(0,len(n)):
    
    count = 0
    if n[i] == n[(i-1)]:
       continue
    else:
      for j in range(0,len(n)):
         if n[i] == n[j]:
           count+=1
      if count > maxcount:
         maxcount=count
         maxchar=n[i]+" "
      elif count == maxcount:
         maxcount=count
         maxchar+=n[i]+" "
print(maxchar)