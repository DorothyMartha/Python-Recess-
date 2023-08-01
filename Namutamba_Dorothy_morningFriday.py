# Assignment : Deadline 01 July 2023 Time 5:00pm EAT
# Create a receipt printing program with GUI interface,
# a more advanced detail earns you more points.
import tkinter as tk

def calculate_total():
    # Get the entered values
    item = item_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())

    # Calculate total cost
    total = quantity * price

    # Display the total
    total_label.config(text="Total: $%.2f" % total)

def generate_receipt():
    # Get the entered values
    item = item_entry.get()
    quantity = int(quantity_entry.get())
    price = float(price_entry.get())

    # Calculate total cost
    total = quantity * price

    # Generate the receipt
    receipt = "Receipt\n\n"
    receipt += "Item: %s\n" % item
    receipt += "Quantity: %d\n" % quantity
    receipt += "Price: $%.2f\n" % price
    receipt += "Total: $%.2f\n" % total

    # Display the receipt
    receipt_text.delete('1.0', tk.END)
    receipt_text.insert(tk.END, receipt)

# Create the GUI
window = tk.Tk()
window.title("Receipt Printing Program")

# Item
item_label = tk.Label(window, text="Item:")
item_label.pack()
item_entry = tk.Entry(window)
item_entry.pack()

# Quantity
quantity_label = tk.Label(window, text="Quantity:")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

# Price
price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Calculate button
calculate_button = tk.Button(window, text="Calculate Total", command=calculate_total)
calculate_button.pack()

# Total
total_label = tk.Label(window, text="Total:")
total_label.pack()

# Generate receipt button
generate_button = tk.Button(window, text="Generate Receipt", command=generate_receipt)
generate_button.pack()

# Receipt
receipt_label = tk.Label(window, text="Receipt:")
receipt_label.pack()
receipt_text = tk.Text(window, height=10, width=40)
receipt_text.pack()

# Run the GUI
window.mainloop()
