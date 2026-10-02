'''3. E-Commerce Offer Engine
   An online store provides multiple offers independently:

* If cart value ≥ 500 → Free delivery
* If cart value ≥ 1000 → 10% discount coupon

Input:
Enter cart value: 1200

Output:
Free delivery applied
Discount coupon unlocked'''

#solution


value = int(input("Enter cart value:"))
if value >= 500:
    print("Free delivery")

    if value >= 1000:
        print("Discount coupon unlocked")
        value = value - (value * 10 / 100)
        print("Discount price:", value)

else:
    print("Happy shopping")