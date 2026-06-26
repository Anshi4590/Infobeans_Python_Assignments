'''9. Neon Number LED Unlock Game
You're programming a new LED display game. The game level unlocks only when a neon number is entered.

A neon number is a number where the sum of the digits of its square is equal to the number itself.
Example: 9 → 9² = 81 → 8 + 1 = 9

Accept a number from the player.
Check whether it is a neon number using loops.

If true, display:
Glowing Success! You've found the Neon Number!

Otherwise display:
Try again! Not quite glowing yet.

Input:
9

Output:
Glowing Success! You've found the Neon Number!'''


#solution


n = int(input("enter the number"))
sum = 0
square = n*n
'''for i in range(len(str(square))):
    digit = square%10
    sum = sum + digit
    square = square//10
print(sum)
if sum == n:
  print("Glowing Success! You've found the Neon Number!")
else:
  print("Try again! Not quite glowing yet.")'''


while square>0:
    digit = square%10
    sum = sum + digit
    square = square//10
print(sum)
if sum == n:
  print("Glowing Success! You've found the Neon Number!")
else:
  print("Try again! Not quite glowing yet.")
















