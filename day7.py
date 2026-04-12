# set and tuple in python


collection={1,2,3,4,"hello","world"}
collection.add(5) # add element 
collection.remove(2) # remove the element an
collection.pop() # remove a random value

print(collection)
print(type(collection))
print(len(collection))

collection1=set() # empty set
print(type(collection1))


a = {1, 2, 3}
b = {3, 4, 5}

a.add(6)
a.remove(1)

print("Union:", a.union(b))
print("Intersection:", a.intersection(b))
print("Difference:", a.difference(b))


 #tuple

a = (1, 2, 3, 2, 4)

print("Count of 2:", a.count(2))
print("Index of 3:", a.index(3))
print("Length:", len(a))
print("Max:", max(a))
print("Sum:", sum(a))



a = (1, 2, 3)        # create a tuple (immutable → cannot change directly)

b = list(a)          # convert tuple into list (list is mutable)

b[0] = 100           # change first element (index 0) from 1 → 100

print(b)             # print updated list