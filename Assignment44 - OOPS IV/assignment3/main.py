from models.product import Product



product_db = []

for i in range(2):

    product_id = int(input("Enter Product ID: "))
    product_name = input("Enter Product Name: ")
    price = int(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    print()

    product = Product(product_id, product_name, price, quantity)

    product_db.append(product)


print("\nAll Products:")

for product in product_db:

    product.display_product()


print("\nProduct Total Values:")

for product in product_db:
    print(f"{product.product_name} {product.total_value()}")


print("\nLow Stock Products:")

for product in product_db:

    if product.is_low_stock:
       product.display_product()



print("\nHighest Price Product:")

high = product_db[0]

for i in product_db:
    if i.high_price(high):

        high =i
high.display_product()


print("\nTotal Inventory Value:")

total = 0
for i in product_db:

    total = i.total(total)

print(total)



id = int(input("\nEnter Product ID to search: "))

for i in product_db:

    if  i.search_id(id):

        print("\nProduct Found:")
        i.display_product()




