# Number 1
names = ["Dorothy", "John", "Benjamin", "Doris", "Julius"]
print("The first name is:", names[0])

# Number 2
names[0] = "Martha"
print("The first name after change is:", names[0])

# Number 3
names.append("Emily")
print("List with a sixth item:", names)

# Number 4
names.insert(2, "Bathel")
print("List with 'Bathel' as the 3rd item:", names)

# Number 5
del names[3]
print("List after removing the 4th item:", names)

# Number 6
print("Last item using negative indexing:", names[-1])

# Number 7
new_list = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grapes"]
print("Items from new_list using range of indexes:", new_list[2:5])

# Number 8
countries = ["USA", "Canada", "UK", "Germany", "France"]
countries_copy = countries.copy()
print("Copy of countries list:", countries_copy)

# Number 9
print("Looping through the list of countries:")
for country in countries:
    print(country)

# Number 10
animal_names = ["Lion", "Tiger", "Elephant", "Giraffe", "Monkey"]
ascending_order = sorted(animal_names)
descending_order = sorted(animal_names, reverse=True)
print("Animal names in ascending order:", ascending_order)
print("Animal names in descending order:", descending_order)

# Number 11
names_with_a = [name for name in animal_names if "a" in name.lower()]
print("Animal names with the letter 'a':", names_with_a)

# Number 12
first_names = ["John", "Alice", "David"]
second_names = ["Smith", "Johnson", "Brown"]
joined_names = first_names + second_names
print("Joined list of names:", joined_names)
print("*********************************************")

#Exercise 2(Tuples)
# Number 1
x = ("samsung", "iphone", "tecno", "redmi")
favorite_brand = x[1]
print("Favorite phone brand:", favorite_brand)

# Number 2
second_last_item = x[-2]
print("Second last item:", second_last_item)

# Number 3
phones = list(x)
phones[1] = "itel"
x = tuple(phones)
print("Updated tuple:", x)

# Number 4
x = x + ("Huawei",)
print("Tuple with 'Huawei' added:", x)

# Number 5
print("Looping through the tuple:")
for item in x:
    print(item)

# Number 6
x = x[1:]
print("Tuple after removing the first item:", x)

# Number 7
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print("Tuple of cities in Uganda:", uganda_cities)

# Number 8
first_city, second_city, third_city, fourth_city, fifth_city = uganda_cities
print("Unpacked tuple:")
print("First city:", first_city)
print("Second city:", second_city)
print("Third city:", third_city)
print("Fourth city:", fourth_city)
print("Fifth city:", fifth_city)

# Number 9
print("2nd, 3rd, and 4th cities:", uganda_cities[1:4])

# Number 10
first_names = ("John", "Alice", "David")
second_names = ("Smith", "Johnson", "Brown")
joined_names = first_names + second_names
print("Joined tuple of names:", joined_names)

# Number 11
colors = ("red", "blue", "green")
multiplied_tuple = colors * 3
print("Multiplied tuple:", multiplied_tuple)

# Number 12
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_of_eight = thistuple.count(8)
print("Number of times 8 appears:", count_of_eight)

print("*********************************************")

#Exercise 3(SETS)
# Number 1
beverages = set(["Bailey's", "Smirnoff", "Nile special"])
print("Beverages set:", beverages)

# Number 2
beverages.add("Coca-Cola")
beverages.add("Tea")
print("Updated beverages set:", beverages)

# Number 3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

# Number 4
mySet.remove("kettle")
print("Set after removing 'kettle':", mySet)

# Number 5
print("Looping through the set:")
for item in mySet:
    print(item)

# Number 6
set_items = {"shoes", "scurf", "orange", "jerrycan"}
list_items = ["brush", "shoelaces"]
set_items.update(list_items)
print("Set after adding list elements:", set_items)

# Number 7
ages = {21, 20, 25}
first_names = {"Lillian", "Joshua", "Rose"}
joined_set = ages.union(first_names)
print("Joined set of ages and first names:", joined_set)
print("*********************************************")
#Exercise 4(STRINGS):
# Number 1
num = 10
text = "Hello"
concatenated = str(num) + " " + text
print(concatenated)

# Number 2
txt = " Hello, Uganda! "
output = txt.strip()
print(output)

# Number 3
txt = "Hello, Uganda!"
uppercase = txt.upper()
print(uppercase)

# Number 4
txt = "Hello, Uganda!"
replaced = txt.replace('U', 'V')
print(replaced)

# Number 5
y = "I am proudly Ugandan"
range_of_characters = y[1:4]
print(range_of_characters)

# Number 6
x = 'All "Data Scientists" are cool!'
print(x)
print("*********************************************")

#Exercise 5(DICTIONARIES):
# Number 1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
shoe_size = Shoes["size"]
print("Shoe size:", shoe_size)

# Number 2
Shoes["brand"] = "Adidas"
print("Updated brand:", Shoes["brand"])

# Number 3
Shoes["type"] = "sneakers"
print("Updated dictionary:", Shoes)

# Number 4
keys = list(Shoes.keys())
print("List of keys:", keys)

# Number 5
values = list(Shoes.values())
print("List of values:", values)

# Number 6
if "size" in Shoes:
    print("The key 'size' exists in the dictionary")
else:
    print("The key 'size' does not exist in the dictionary")

# Number 7
print("Looping through the dictionary:")
for key, value in Shoes.items():
    print(key, ":", value)

# Number 8
del Shoes["color"]
print("Dictionary after removing 'color':", Shoes)

# Number 9
Shoes.clear()
print("Empty dictionary:", Shoes)

# Number 10
my_dict = {"name": "Dorothy", "age": 22}
copy_dict = my_dict.copy()
print("Copy of the dictionary:", copy_dict)

# Number 11
nested_dict = {
    "person1": {
        "name": "Martha",
        "age": 25
    },
    "person2": {
        "name": "Sarah",
        "age": 56
    }
}
print("Nested dictionary:", nested_dict)



