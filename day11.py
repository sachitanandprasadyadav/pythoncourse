class Parent():
    a=100
    b=1000

    def __init__(self,a,b):
        print("this is cons from parents")
        


    def add(self):
        return self.a+self.b
    
class child(Parent):
    def __init__(self, a, b):
        print("this is cons from child")
        super().__init__(a, b)
    def result(self):
        return self.add()
    

obj=child(1,2)
print(obj.result())    


#multi level
print("----------------------------*2")
class GrandChild(child):
    def summary(self):
        return "this is summmary data"
obj=GrandChild(1,1)
print(obj.add())    




class Person:
    name="sachin"
    age=22

    def display_info(self):
        return f"name is {self.name} age is {self.age}"
    
    def display_info_np(self):
        return f"mero name {self.name}, ani mero age ho {self.age}"

class Student(Person):
    student_id=123





    def display_student(self):
        return f"student_id{self.student_id},{self.display_info()}"    
    

class GraduateStudent(Student):
    thesis_topics="IT"

    def display_graduate(self):
        return f"thesis_id {self.thesis_topics},{self.display_student()}"
    
obj=GraduateStudent()
print(obj.display_graduate())











class test():
    a=100


class test2():
    b=1000


class child(test,test2):
    c=10000

obj=child()
obj.test=1
print(child.__mro__)





class Person:
    name = ""
    age = 0

    def setPerson(self, name, age):
        self.name = name
        self.age = age

    def displayPerson(self):
        return self.name, self.age


class Job:
    jobTitle = ""
    salary = 0

    def setJob(self, jobTitle, salary):
        self.jobTitle = jobTitle
        self.salary = salary

    def displayJob(self):
        return self.jobTitle, self.salary


class Employee(Person, Job):

    def displayEmployee(self):
        name, age = self.displayPerson()
        jobTitle, salary = self.displayJob()

        return f"Name: {name}, Age: {age}, Job: {jobTitle}, Salary: {salary}"


# create object
obj = Employee()

# set values
obj.setPerson("Ram", 25)
obj.setJob("Manager", 50000)

# display result
print(obj.displayEmployee())





class public():
    __a="this is private data"
    b=__a


class Test(public):
    d=2

obj=Test()
print(obj.b)

"""
 Class Account
Private data members:

accountNumber

balance

Public methods:

setAccount() → input account number and balance

deposit(amount) → add money

getBalance() → return balance

displayAccount() → show account number and balance

 Class SavingsAccount (inherits from Account)
Private data member:

interestRate

Public methods:

setSavingsDetails() → input interest rate

calculateInterest() → compute interest using balance

interest = balance * rate / 100
displaySavings() → display all account + interest info

⚠️ Constraint:

You cannot directly access balance (it is private in Account)

You must use public methods like getBalance()

 Class PremiumSavings (inherits from SavingsAccount)
Private data member:

bonus

Public methods:

setBonus() → input bonus amount

calculateTotalBalance() →

total = balance + interest + bonus
displayPremiumDetails() → display full details


"""

class Account:
    def setAccount(self, acc_no, balance):
        self.__accountNumber = acc_no   
        self.__balance = balance        
    def deposit(self, amount):
        self.__balance += amount

    def getBalance(self):
        return self.__balance

    def displayAccount(self):
        print("Account Number:", self.__accountNumber)
        print("Balance:", self.__balance)



class SavingsAccount(Account):
    def setSavingsDetails(self, rate):
        self.__interestRate = rate   

    def calculateInterest(self):
        return self.getBalance() * self.__interestRate / 100

    def displaySavings(self):
        self.displayAccount()
        print("Interest Rate:", self.__interestRate, "%")
        print("Interest:", self.calculateInterest())


 
class PremiumSavings(SavingsAccount):
    def setBonus(self, bonus):
        self.__bonus = bonus   

    def calculateTotalBalance(self):
        return self.getBalance() + self.calculateInterest() + self.__bonus

    def displayPremiumDetails(self):
        self.displaySavings()
        print("Bonus:", self.__bonus)
        print("Total Balance:", self.calculateTotalBalance())

 
p = PremiumSavings()

p.setAccount(101, 5000)
p.setSavingsDetails(5)
p.setBonus(1000)

print("\n--- Premium Account Details ---")
p.displayPremiumDetails()
