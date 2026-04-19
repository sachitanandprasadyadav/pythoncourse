#create a class student with a constructor that initializes name and age.print the value

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Student("sachin", 22)

print(obj.name)
print(obj.age)


#create a class car with a constructor that initiazlies brand and price display the detail

class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def display(self):
        return self.brand, self.price   # returning values

obj = Car("tata", 2000)

result = obj.display()
print(result)

"""
create a class circle
.constructor initializes radius
.method to calculate area
"""

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 22/7 * self.r * self.r

obj = Circle(5)
result = obj.area()
print(result)



"""
create a class bankacount:
.constuctor initi
.account_holder and balance
.method to desposite
"""

class BankAcount:
    def __init__(self,account_balance,balance):
        self.account_balance=account_balance
        self.balance=balance


    def desposit(self,amount):
        self.balance +=amount
        return self.balance



obj=BankAcount("sachin",50000)
result=obj.desposit(4000)
print(result)       
print("account holder name:",obj.account_balance) 
print("balance:",obj.balance)
        
"""
class a class person
.constuctor sets name and age
.method to check if person is adult

"""

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def display(self):
        if self.age>=18:
            return "person is adult"
        else:
            return "person is not adult"


obj=Person("sachin",16)
print(obj.display())      


"""
create a class passwordManager:
.constructor sets password
.method to check if entered password
is correct

"""

class PasswordManager:
    def __init__(self,password):
        self.password=password


    def display(self,enter_password):
        if self.password==enter_password:
            return "password is corrected"
        else:
            return "password is not corrected"
        
obj=PasswordManager(123456)
print(obj.display(123456))
print(obj.display(456789))
        

        
"""
create a class product:
.constuctor takes:
.product name
.quantity
.price
.inside constructor
.valid quantity >_0
.methods:
.add_stock()
.sell_product()
"""
        
class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.price = price

        # validate quantity
        if quantity >= 0:
            self.quantity = quantity
        else:
            self.quantity = 0
            print("Invalid quantity! Set to 0")

    def add_stock(self, amount):
        if amount > 0:
            self.quantity += amount
            return f"Stock added. New quantity: {self.quantity}"
        else:
            return "Invalid stock amount"

    def sell_product(self, amount):
        if amount <= 0:
            return "Invalid sell amount"

        if amount > self.quantity:
            return "Not enough stock"

        self.quantity -= amount
        return f"Sold {amount}. Remaining stock: {self.quantity}"
    
obj = Product("Pen", 10, 20)

print(obj.add_stock(5))
print(obj.sell_product(3))
print(obj.sell_product(20))



"""
create a class Employee:
.name
.basic salary
.inside constuctor:
.calculate:
> hra=20%
>da =10%
>total salary
.method:
.display salary breakdown

"""

class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

        self.hra = 0.20 * basic_salary
        self.da = 0.10 * basic_salary
        self.total_salary = basic_salary + self.hra + self.da

    def get_salary_breakdown(self):
        return {
            "Employee Name": self.name,
            "Basic Salary": self.basic_salary,
            "HRA": self.hra,
            "DA": self.da,
            "Total Salary": self.total_salary
        }


obj = Employee("Sachin", 50000)

result = obj.get_salary_breakdown()
print(result)

"""
create a class student:
.constructor takes:
.name
.rollnumber
.list of marks
 .inside constructor
 .calculate total,averge,grade

 .method :
 display report

"""
class Student:
    def __init__(self, name, rollnumber, listofmarks):
        self.name = name
        self.rollnumber = rollnumber
        self.marks = listofmarks

        self.total = sum(self.marks)
        self.average = self.total / len(self.marks)

        if self.average >= 90:
            self.grade = "A"
        elif self.average >= 75:
            self.grade = "B"
        elif self.average >= 50:
            self.grade = "C"
        else:
            self.grade = "F"

    def get_report(self):
        return {
            "Name": self.name,
            "Roll Number": self.rollnumber,
            "Marks": self.marks,
            "Total": self.total,
            "Average": self.average,
            "Grade": self.grade
        }
    

obj = Student("Sachin", 101, [80, 90, 85, 70])

report = obj.get_report()
print(report)


    


""""





"""








        



        

