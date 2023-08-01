# Assigning variables 
name = "Dorothy Martha"
age = 25
is_female = True
height_cm = 180.3

# Output variable values
print("Name:", name)
print("Age:", age)
print("Is Female:", is_female)
print("Height (in cm):", height_cm)

# reassigning variables
age = age + 5
height_m = height_cm / 100

# Updated variable values
print("\nUpdated Age:", age)
print("Height (in meters):", height_m)

# swapping variables
x = 10
y = 5
print("\nBefore swapping: x =", x, "y =", y)
x, y = y, x
print("After swapping: x =", x, "y =", y)

# concatenating variables
greeting = "Hello"
subject = "Dorothy"
message = greeting + ", " + subject + "!"
print("\nMessage:", message)

# Variable interpolation
quantity = 10
price = 2.5
total = quantity * price
print("Total:", total)

# Variable scope
def my_function():
    local_var = "I am a local variable"
    print("\nInside the function:", local_var)

my_function()

