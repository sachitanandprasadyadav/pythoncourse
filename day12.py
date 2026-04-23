file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

file = open("data.txt", "w")
file.write("this is data")
file.close()


file = open("data.txt", "a")
file.write("\nsachin")
file.close()






import csv

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    print(reader)
    for index,row in enumerate(reader):
        print(index+1,row)


        
with open("students.txt", "a") as file:
    name = input("Enter name: ")
    age = input("Enter age: ")
    
    file.write(f"{name},{age}\n")