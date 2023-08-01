import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += symbol
    equation.set(calculation)

def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))
        equation.set(result)
        calculation = result
    except Exception as e:
        equation.set("Error")
        calculation = ""

def clear_field():
    global calculation
    calculation = ""
    equation.set("")

def multiply():
    add_to_calculation("*")

def divide():
    add_to_calculation("/")

def subtract():
    add_to_calculation("-")

def add():
    add_to_calculation("+")

root = tk.Tk()
root.title("Dorothy_Martha")
root.geometry("400x450")

equation = tk.StringVar()
display_field = tk.Entry(root, textvariable=equation, width=20, font=("Arial", 20))
display_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

operations = {
    "/": divide,
    "*": multiply,
    "-": subtract,
    "+": add
}

row_index = 1
col_index = 0

for text in button_texts:
    if text == "=":
        btn = tk.Button(root, text=text, width=10, height=2, font=("Arial", 14),
                        command=evaluate_calculation)
    elif text in operations:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=operations[text])
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda symbol=text: add_to_calculation(symbol))

    btn.grid(row=row_index, column=col_index, padx=5, pady=5)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

clear_btn = tk.Button(root, text="Clear", width=10, height=2, font=("Arial", 14),
                      command=clear_field)
clear_btn.grid(row=row_index, column=col_index, columnspan=4, padx=10, pady=5)

root.mainloop()
