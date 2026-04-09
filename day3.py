#condition statements


#grade student based on marks

marks = int(input("enter student marks : "))

if marks >= 90:
    grade = "A"
elif marks >= 80 and marks < 90:
    grade = "B"
elif marks >= 70 and marks < 80:
    grade = "C"
else:
    grade = "D"

print("grade of the student =>", grade)




#waptto check if number entered by user is odd or even

num=int(input("enter the number"))

if num%2==0:
    print("number is even:",num)

else:
    print("number is odd:",num)




#wap to find the greater of 3 number entered by the user

# Taking input from user
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Checking largest number
if (a >= b and a >= c):
    print("First number is largest:", a)

elif (b >= c):
    print("Second number is largest:", b)

else:
    print("Third number is largest:", c)     




    