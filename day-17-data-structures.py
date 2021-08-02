print('Creating a Tuple...............................................')
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

# Creating a set fro a list (to remove duplicates from a list).

print('Creating a set.................................................')
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_elements = set(numbers)
print(unique_elements)

print('Creating another set...........................................')
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set

print("watermelon" in fruit)  # check for element

fruit.add("watermelon")  # add an element
print(fruit)

print(fruit.pop())  # remove a random element
print(fruit)

print('Creating a dictionary..........................................')
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}

print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the
# dictionary

print("carbon" in elements)
print(elements.get("dilithium"))
