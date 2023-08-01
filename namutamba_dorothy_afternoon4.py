#Functions
def afternoon(first_name, last_name):
    print(f"Good afternoon, {first_name} {last_name}!")

#calling a function
afternoon("Owen", "Marvin")
print("****************************************************************")

def greet():
    print("Hello! Welcome.")

def add_numbers(a, b):
    return a + b

def square_number(num):
    return num ** 2

# Call the greet function
greet()

# Call the add_numbers function and store the result
result = add_numbers(5, 3)
print("Sum:", result)

# Call the square_number function and print the result
number = 4
square_result = square_number(number)
print(f"The square of {number} is {square_result}.")


