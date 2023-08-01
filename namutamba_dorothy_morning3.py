# Prompt the user for two numbers
#x = float(input("Enter the first number: "))
#y = float(input("Enter the second number: "))
x = 20
y = 30
# Perform arithmetic operations
sum_result = x + y
difference_result = x - y
product_result = x * y
quotient_result = x / y
remainder_result = x % y
power_result = x ** y

# Display the results
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)
print("Remainder:", remainder_result)
print("Power:", power_result)
print("****************************************************************")
#Comparison operators

h = 10
r = 5
#Greater than
if h > r:
    print("h is greater than r")  # Checking if h is greater than r
#Less than
if h < r:
    print("h is less than r")  # Checking if h is less than r
#Greater than or equal
if h >= r:
    print("h is greater than or equal to r")  # Checking if h is greater than or equal to r
#Less than or equal
if h <= r:
    print("h is less than or equal to r")  # Checking if h is less than or equal to r
#Equal to
if h == r:
    print("h is equal to r")  # Checking if h is equal to r
#Not equal to
if h != r:
    print("h is not equal to r")  # Checking if h is not equal to r

print(h==r)
print(r!= h)

print("****************************************************************")

#Logical operators
# Assign values to k and m
k = True
m = False

# Logical and 
print("Logical and:", k and m)
# Logical or
print("Logical or:", k or m)
#logical not
print("Logical not K:", not k)
#Logical not M:", not m)
print("Logical not m", not m)
print("****************************************************************")

#Assignment operators
a = 5
b = 3
# Print the result
print("Initial values: a =", a, "b =", b)
 # Add and assign
a += b 
print("After a += b: a =", a)
 # Subtract and assign
a -= b 
print("After a -= b: a =", a)
# Multiply and assign
a *= b  
print("After a *= b: a =", a)
# Divide and assign
a /= b  
print("After a /= b: a =", a)
# Modulus and assign
a %= b  
print("After a %= b: a =", a)
# Exponentiation and assign
a **= b  
print("After a **= b: a =", a)
print ("****************************************************************")

#Membership assignment operators
# Define an array of kids' toys
toys = ["Doll", "Car", "Puzzle", "Teddy Bear"]

toy = "Car"
if toy in toys:
    print(toy, "is in the array")
else:
    print(toy, "is not in the array")

toy = "Ball"
if toy not in toys:
    print(toy, "is not in the array")
else:
    print(toy, "is in the array")

print("****************************************************************")
# Define two variables with the same value
x = 12
y = 12

# Identity operators
print("x is y:", x is y)
print("x is not y:", x is not y)
print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x <= y:", x <= y)
print("x > y:", x > y)
print("x >= y:", x >= y)
print("****************************************************************")
# Define two integers
a = 10  # binary: 1010
b = 6   # binary: 0110

# Bitwise AND
result_and = a & b
print("Bitwise AND:", result_and)  # Output: 2 (binary: 0010)

# Bitwise OR
result_or = a | b
print("Bitwise OR:", result_or)    # Output: 14 (binary: 1110)

# Bitwise XOR
result_xor = a ^ b
print("Bitwise XOR:", result_xor)  # Output: 12 (binary: 1100)

# Bitwise NOT
result_not = ~a
print("Bitwise NOT:", result_not)  # Output: -11 (binary: 11111111111111111111111111110101)

# Left Shift
result_left_shift = a << 2
print("Left Shift:", result_left_shift)  # Output: 40 (binary: 101000)

# Right Shift
result_right_shift = a >> 2
print("Right Shift:", result_right_shift)  # Output: 2 (binary: 10)





