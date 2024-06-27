# SETS

# s = {"a", "b", "c", "d"}
# print(type(s))

# Using the set method to create sets
# s1 = set(["a", "b", "c", "d","e"])
# print(s1)

# Adding elements to sets
# s2 = set(["a", "b", "c", "d", "python"])
# s2.add((1,2,3,4))
# print(s2)

# # Frozen sets (immutable sets). Cannot add to the set.
# s3 = frozenset([1,2,3,4])
# print(s3)

# Union of sets
s4 = set([1,2,3,4,5,8])
s5 =  set([5, 6, 7, 8])
s_u = s4.union(s5)
print(s_u)

# Difference in sets
s_d = s4.difference(s5)
print(s_d)

# Used to perform symmetric difference in sets (removing what is common in both sets.)
print(s4 ^ s5)

# Operators in sets
print(s4 == s5)

print(s4 > s5)

