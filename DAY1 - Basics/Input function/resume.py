'''3. Resume Format
Write a program to display:
=== Resume ===
Name       : Alice Johnson
Email      : alice@example.com
Skills     :
  - Java
  - HTML & CSS
  - Problem Solving
Experience : 2 years at XYZ Ltd.'''

print("=== Resume ===")
name = "Alice Johnson"
email = "alice@example.com"
Skill1 = "- Java"
Skill2 = "- HTML & CSS"
Skill3 = "- Problem solving"
experience = "2 years at xyz Ltd"
print ("Name\t:",name)
print ("Email\t:",email)
print (f"skills\t:\n{Skill1}\n{Skill2}\n{Skill3}")
print ("Experience\t:",experience)