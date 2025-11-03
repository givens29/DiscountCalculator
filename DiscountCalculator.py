import tkinter as tk
from tkinter import messagebox

def calculateDisc():
    try:
        priceInput = priceField.get().replace('.', '')
        price = int(priceInput)
        discRate = float(discField.get())
        quantity = int(quantityField.get())

        subtotal = price * quantity
        discAmount = subtotal * (discRate / 100)
        totalPrice = subtotal - discAmount

        formatPrice = f"Rp {price:,.0f}".replace(',', '.')
        formatTotal = f"Rp {totalPrice:,.0f}".replace(',', '.')

        receipt = (
            f"------------------\n"
            f"Price for an item: {formatPrice}\n"
            f"Quantity: {quantity}\n"
            f"Discount rate: {discRate}%\n"
            f"Total after discount: {formatTotal}\n"
            f"-------------------\n"
            f"Thank you for shopping with us!"
        )

        messagebox.showinfo("Receipt", receipt)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


root = tk.Tk()
root.title("Discount Calculator")
root.geometry("400x300")

greetings = tk.Label(root, text="Welcome to the Discount Calculator!", font=("Arial", 10))
greetings.pack(pady=20)

tk.Label(root, text="Original Price (ex: 2.000.000):").pack(pady=5)
priceField = tk.Entry(root)
priceField.pack()

tk.Label(root, text="Discount Rate (%)").pack(pady=5)
discField = tk.Entry(root)
discField.pack()

tk.Label(root, text="Quantity:").pack(pady=5)
quantityField = tk.Entry(root)
quantityField.pack()

calculateButton = tk.Button(root, text="Calculate", command=calculateDisc)
calculateButton.pack(pady=15)

root.mainloop()