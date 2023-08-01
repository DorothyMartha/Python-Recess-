#first declare a variable
age = int(input("Enter your age: "))
if age<18:
    print("You're under age")
elif age>=18 and age <=65:
    print("You're an adult")
else:
    print("You're not a senior citizen")