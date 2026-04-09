# Python List Functions - All in One Example

# Create list
a = [3, 1, 2]
print("Original list:", a)

# append()
a.append(4)
print("After append(4):", a)

# insert()
a.insert(1, 10)
print("After insert(1, 10):", a)

# extend()
a.extend([5, 6])
print("After extend([5, 6]):", a)

# remove()
a.remove(10)
print("After remove(10):", a)

# pop()
a.pop()
print("After pop():", a)

# index()
print("Index of 2:", a.index(2))

# count()
a.append(2)
print("After adding another 2:", a)
print("Count of 2:", a.count(2))

# sort()
a.sort()
print("After sort():", a)

# reverse()
a.reverse()
print("After reverse():", a)

# copy()
b = a.copy()
print("Copied list:", b)

# clear()
a.clear()
print("After clear():", a)