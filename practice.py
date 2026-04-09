"""Create a list of 5 numbers and print it  (list question)
Add a new element to the list
Remove an element from the list
Print the first and last element
🔹 Medium
Find the largest number in a list
Count how many times a number appears
Reverse a list without using built-in function
Sort a list (ascending order)

Merge two lists into one"""


data=[1,2,3,4,5]
print(data)
data.append(6)
print(data)

data.remove(4)
print(data)
print(data[0],data[-1])

print(max(data))
print(data.count(2))
print(data[::-1])
print(sorted(data))

list2=[6,7,8,9]
print(data+list2)

""" 
 Create a dictionary called student with keys: "name", "age", "course" and give them some values.
Print the value of "name" from the dictionary.
Add a new key "city" with any value.
Update the "age" to a new value.
Remove the key "course" from the dictionary.
Print all keys of the dictionary.
Print all values of the dictionary."""



student={
    "name":"sachin",
    "age":"22",
    "course":"Bim"
}

print(student["name"])
student["city"]="birgunj"
print(student)

student["age"]=22
print(student)

student.pop("course")
print(student)




# for loop
#range

"""print the element of the following list using a loop
calculate the sum of number in alist
print each charater of a string """


nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)

nums1=[1,2,3,4,5]
total=0
for num in nums1:
    total+=num
print("sum",total)       

word="sachin"
for char in word:
    print(char)


#range

"""print even number from 2 to 20
print number in reverse from 10 to 1
count vowels in a string "programming" """

for i in range(2,21,2):
    print(i,end="")

for i in range(10,0,-1):
    print(i)



text="programming"
vowels="aeiou"
count=0

for char in vowels:
    count+=1
print("vowel count:",count)    