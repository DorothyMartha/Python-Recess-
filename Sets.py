# Creating a set of furniture items
furniture_set = {"chair", "table", "bed", "cupboard"}

# Length of the set
print("Length of the furniture set:", len(furniture_set))

# Data type of the set
print("Data type of the furniture set:", type(furniture_set))

# Accessing elements in the set
for item in furniture_set:
    print("Furniture item:", item)

# Adding items to the set
furniture_set.add("sofa")
furniture_set.add("lamp")
print("Updated furniture set:", furniture_set)

# Creating another set
additional_set = {"shelf", "mirror"}

# Combining two sets (Union)
combined_set = furniture_set.union(additional_set)
print("Combined set:", combined_set)
