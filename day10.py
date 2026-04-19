#create student class that takes name and marks of 3 subjects as agrument in constructor then create a method to print the average

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_averge(self):
        sum=0
        for val in self.marks:
            sum +=val
        print("hi",self.name,"your avg score is :",sum/3)    

s1=Student('sachin',[89,90,65])   
s1.get_averge()     
        

        
#single Inheritance

class Parent:
    def show(self):
        print("This is parent class")

class Child(Parent):   # Child inherits Parent
    def display(self):
        print("This is child class")

obj = Child()
obj.show()     # inherited method
obj.display()  # own method





#inheritance 


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
