#function


def hello():
    print("Hello Python")

hello()   # function call




def greet(name):
    print("Hello", name)

greet("Sachin")



def add(a, b):
    return a + b
result = add(10, 20)
print(result)



def sum_list():
    data = [1, 2, 3, 4]
    total = 0
    for i in data:
        total += i
    return total

print(sum_list())




def test():
    a = 10   # local variable
    print(a)

test()



a = 50   # global variable

def test():
    print(a)

test()







def testing():
    a = [1, 2, 3, 4, 5, 6]
    global datas
    datas = 100
    print(datas)

    for i in a:
        data = i   # stores last value

    return i   # last value of loop

print(testing())
print(datas)





def greet(name="User"):
    print("Hello", name)

greet()         # default value
greet("Ram")    # custom value