'''43 Check if two strings are rotations of each other. 
   S1 = "abcde", S2 = "cdeab" 
   output - TRUE'''


s1 = input("Enter String : ")
s2 = input("Enter String : ")

m = list(s1)
first=""

if len(s1) == len(s2):
   for i in range(len(s1)): # this loop start from index 0
      last = i
      new =""
      
      for j in range(i+1,len(m)): # this loop will Start from index i+1 till len of m
         new+=m[j]
      new+=first+s1[last]

      if s2 == new: # here it will check the rotated string with s2
         print(("True"))
         break

      first+= s1[last] # this will add the previous substring

   if s2!= new:
      print("false")
   
else:
   print("False")
  