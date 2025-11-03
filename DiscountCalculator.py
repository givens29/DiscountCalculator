print("Welcome to the Discount Calculator!\n")

price_input = input("Enter the original price of an item \n (ex: 2.000.000): Rp ")
discount_rate = float(input("Enter the discount rate in %: "))
quantity = int(input("Enter the quantity of items: "))

price = int(price_input.replace(".", ""))
subtotal = price * quantity
discountAmount = subtotal * (discount_rate / 100)
total = subtotal - discountAmount

formatPrice = f"Rp {price:,.0f}".replace(",", ".")
formatTotal = f"Rp {total:,.0f}".replace(",", ".")

print("\n----- Receipt -----")
print(f"Price for an item: {formatPrice}")
print(f"Quantity: {quantity}")
print(f"Discount rate: {discount_rate}%")
print(f"Total after discount: {formatTotal}")
print("-------------------\n")

print(f"Thank you for shopping with us!")