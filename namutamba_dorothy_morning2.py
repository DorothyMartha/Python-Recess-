# If Statement
temperature = 27

if temperature > 30:
    print("It's a hot day!")
elif temperature > 20:
    print("It's a pleasant day.")
else:
    print("It's a bit chilly.")

# For Loop
superheroes = ["Spider-Man", "Iron Man", "Wonder Woman"]
for hero in superheroes:
    print("I admire", hero)

# While Loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# Break Statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print("Found the number 3!")
        break
    print(num)

# Continue Statement
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print(num)

# Pass Statement
def my_function():
    pass

# Try-Except Statement
numerator = 10
denominator = 0

try:
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero")
else:
    print("Result:", result)

print("Program continues...")


#EXERCISE (Mental Health)
# Prompt the user for their name
name = input("Enter your name: ")

# Prompt the user for their mental health state value
value = int(input("Enter your mental health state value (1-10): "))

# Define a dictionary with comments for each mental health state value
comments = {
    1: "Sorry you're feeling this way. Reach out for support.",
    2: "It's tough, but you're not alone. Seek help from loved ones or professionals.",
    3: "Take care of yourself. Consider self-care activities and talk to someone.",
    4: "Acknowledge your feelings. Seek guidance if needed.",
    5: "Stay positive and surround yourself with positivity.",
    6: "Maintain balance and practice mindfulness.",
    7: "Keep up the good work! Take breaks and prioritize self-care.",
    8: "You're doing well! Continue to nurture your mental well-being.",
    9: "Great job! Stay resilient and maintain a positive mindset.",
    10: "You're in an excellent mental state! Keep thriving!"
}

# Check if the value is within the valid range
if value < 1 or value > 10:
    print("Invalid mental health state value. Please enter a value between 1 and 10.")
else:
    # Retrieve the comment from the dictionary based on the mental health state value
    comment = comments[value]
    
    # Display the personalized message
    print(f"{name}, {comment}")
