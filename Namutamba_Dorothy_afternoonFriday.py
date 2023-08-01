# Append to a file ('a' mode)
with open('file.txt', 'a') as file:
    file.write('This is a sample text.\n')

# Read from a file ('r' mode)
with open('file.txt', 'r') as file:
    content = file.read()
    print("Read mode ('r') content:\n", content)

# Write to a file ('w' mode)
with open('file.txt', 'w') as file:
    file.write('This will overwrite the previous content.\n')

# Append and read from a file ('a+' mode)
with open('file.txt', 'a+') as file:
    file.write('This is an additional line.\n')
    file.seek(0)  # Move the file cursor to the beginning
    content = file.read()
    print("Append and read mode ('a+') content:\n", content)

# Read and write to a file ('r+' mode)
with open('file.txt', 'r+') as file:
    content = file.read()
    print("Read and write mode ('r+') content:\n", content)
    file.write('This is a new line.\n')

# Write and read from a file ('w+' mode)
with open('file.txt', 'w+') as file:
    file.write('This will overwrite the previous content.\n')
    file.seek(0)  # Move the file cursor to the beginning
    content = file.read()
    print("Write and read mode ('w+') content:\n", content)

# Exception handling
try:
    x = 10/0
except ZeroDivisionError:
    print('Error: Division by zero') #cannot divide by zero
finally:
    print('This is always executed') #complete execution  