data = {
    "name": "sachin",     # first value (will be overwritten)
    "age": 22,            # integer value
    "city": "birgunj",    # string value
    "name": "dipesh"      # duplicate key → replaces "sachin"
}

# Print the dictionary
print(data)               # {'name': 'dipesh', 'age': 22, 'city': 'birgunj'}

# Print the type
print(type(data))         # <class 'dict'>

# Print number of items
print(len(data))          # 3

#  Update age
data["age"] = 23          # change value from 22 to 23

# Print updated age
print(data["age"])   


data["number"]=600
print(data)  


# Update dictionary with new values
data.update(
    {
        "name": "bikash",     # update existing key
        "number1": 7000,      # add new key
        "address": "nagawa",  # add new key
        "suname": "yadav"     # add new key (typo: should be 'surname')
    }
)

# Print updated dictionary
print(data)

print(data.keys())
print(data.values())


#delete a key-value pair
del data["number1"] # delete key "number1" and it s value
print(data)

# pop a key -value pair 
data.pop("address") # delete key address and its value
print(data)

# popitem()
data.popitem() # delete last inserted key-value pair
print(data)


data.clear() # clear all key value pair
print(data)

data.get("name") # returns none since the dictionary is empty
print(data)


