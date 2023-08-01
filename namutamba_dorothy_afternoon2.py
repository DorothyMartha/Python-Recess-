person = {
    "name": "Dorothy",
    "id": 345,
    "district": "Jinja"
}
#access values in a dictionary
print(person["name"])
print(person["id"])
print(person["district"])
print ("****************************************************************")



#Exercise one
my_list= list(person.values())
print(my_list)
print ("****************************************************************")

#Exercise two
#check if key exists in the dictionary, use "in" key word
if "name" in person:
    print ("Name already in dictionary")
if "dance" in person:
    print ("Dance already in dictionary")
else:
    print ("Dance is an Unknown dictionary key")

print ("****************************************************************")

#Exercise three
#you can modify the values in a dictionary by assigning a new value to a specific key
person["name"] = "Martha"
person["id"] = 35
print (person["id"])
print (person["district"])
print ("****************************************************************")
#how to update using the update() function
new_items = {
    "occupation": "Teacher",
    "country": "United States"
     }
person.update(new_items)
print (person)
print ("****************************************************************")

#Exercise four 
#to add a new key value pair to the dictionary, assign a value to a new key
person["occupation"] = "Software Engineer"
print(person["occupation"])
print ("****************************************************************")

#remove item from dictionary
#using del
#del person["occupation"]
#print (person)

#using pop()
removed_item = person.pop("occupation")
print (removed_item)
print (person)

print ("****************************************************************")

#Exercise on Numbers
# 1. convert from int to float
b =15
b_float = float(b)
print (b_float)
print ("****************************************************************")

#2. convert from float to complex
a = 3.5
a_complex = complex(a)
print (a_complex)
print ("****************************************************************")

#3. convert from complex to float
x = 2 + 3j
#x_float = float(x) #this will raise a type error
#so to do this conversion, we need to extract the real or imaginary part of the complex value
#using the real part of the complex
x_real = x.real
x_float = float(x.real)
print (x_float)
print ("****************************************************************")
#using the imaginary part of the complex
x_imaginary = x.imag
x_float = float (x_imaginary)
print (x_float)
print ("****************************************************************")

#Exercise on Strings
#Exercise one
str = "Truth is, python is quite interesting!"
length = len(str)
print (length)
print ("****************************************************************")

#Exercise two(for loop)
str2 = "Hello, Dora"
for char in str2: print (char)
print ("****************************************************************")

#Exercise three(slicing in strings)
str3 = "Dorothy Martha"
#Slicing to extract substrings
a = str3[0:7]
b = str3[8:]
c = str3[::-1]
print (a)
print (b)
print (c)
print ("****************************************************************")
#Exercise on boolean
age = int(input("Enter your age: "))

if age<18:
    print("You're under age")
elif age>=18 and age <=65:
    print("You're an adult")
else:
    print("You're not a senior citizen")
    
