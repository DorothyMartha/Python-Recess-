#Regular expressions
#Validating an email
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

# Usage
email = 'dorotheekarma256@gmail.com'
if validate_email(email):
    print('Email is valid.')
else:
    print('Email is invalid.')

print ("*****************************************************************")

#Returning true or false
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    if match:
        return True
    else:
        return False

# Usage
email1 = 'dorotheekarma256@gmail.com'
email2 = 'invalid_email'
email3 = 'dorothy.martha@example'
email4 = 'this@example.com'

print(validate_email(email1))  # Output: True
print(validate_email(email2))  # Output: False
print(validate_email(email3))  # Output: False
print(validate_email(email4))  # Output: True


#generators and iterators
def factorial_generator(n):
    if n == 0:
        yield 1
    else:
        factorial = 1
        for num in range(1, n + 1):
            factorial *= num
            yield factorial

# Using the generator
factorial_sequence = factorial_generator(10)
for num in factorial_sequence:
    print(num)

print ("*****************************************************************")

#Example 3
#Generate a function that yields the square of a number in the range of 1-10
def square():
    for num in range(1, 11):
        yield num ** 2

# Using the generator
squares = square()
for num in squares:
    print(num)

print ("*****************************************************************")
#using the iterator
squares = square()
for num in squares:
    print(num)

print ("****************************************************************")
#decorators
def my_decorator(func):
    def outer():
        print("I am an outer decorator")

        def inner():
            print("I am an inner decorator")
            func()

        inner()

    return outer

@my_decorator
def my_function():
    print("Sir, I hope you are doing great?")

# Using the decorated function
my_function()


