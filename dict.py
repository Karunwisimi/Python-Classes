# # Dictionary
# # Empty Dictionary
# d1 = {}
# print(type(d1))

# #  Dictionary with multiple data types
# d2 = {1.0 :"Python", 2 : "Java", 3 : "Javascript", 4 : "SQL"}
# print(d2)

# d3 = {
#     "key_name":"value_pair",
#     "name": "Simi",
#     "course":"Python_101"
# }
# print(d3)

# Using dictionary methods
# d4 = dict(
#     {
#     1 :"Python",
#     2 : "Java",
#     3 : "Javascript",
#     4 : "SQL"
# }
#           )
# print(d4)

# Creating a dictionary with a list and tuples
# d5 = dict(
#     [
#         (1, "Python"), (2, "Java"), (3, "SQL"), (4, "Devops")
#      ]
# )
# print(d5)

# Creating a nested dictionary
# d6 = {
#     "name" :{"first" : "Simi", "last" : "Karry"},
#     "age" : 22,
#     "profession" : "Cloud Engineer"
# }
# print(d6)

# Adding elements to your dictionary
d7 = {}
d7[0] = "Welcome"
# print(d7)

d7[1] = ("How", "are", "you", 2)
# print(d7)

d7["name"] = "Simi"
# print(d7)
# Updating it
d7["name"] = {"first" : "Simi", "last" : "Karr"}
print(d7)


# Accessing elements in dictionaries
# print(d7)
# print(d7["name"])
# print(d7["name"]["first"])

# Using the .get function to access elements in dictionaries
# print(d7.get(0))

# Deleting elements
# print(d7)

# d7.pop("name")
# print(d7)

# Removes the last element in your dictionary
# d7.popitem()
# print(d7)

# # Dictionary built in functions
# d_v = d7.values()
# print(d_v)

# keys = {"a","b", "c", "d"}
# value = 1
# d_fk = dict.fromkeys(keys,value)
# print(d_fk)

# keys = {"a","b", "c", "d"}
# value = {50, 30, 10}
# d_fk1 = dict.fromkeys(keys,value)
# print(d_fk1)

# clearing the dictionary
d7.clear()