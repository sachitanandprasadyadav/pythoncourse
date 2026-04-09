
"""
for i in <str,list,dict,range>:
    print(i)
    """

for i in "sachin":
    print(i)    


for i in [1,2,3,4,5,6,7,8,9]:
    print(i)   



data = {
    "name": "sachin",     
    "age": 22,            
    "city": "birgunj",    
    
}


for i in data:
    print(f'{i}={data[i]}')


for i in [1,2,3,4,5,6]:
    if i%2==0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')



for i in range(1,100,1):
    if i%2==0:
        print(f'{i}')


for i in range(20):
    if i==5:
        continue
    print(i)     



a=[1,2,"hello","test",1.2,"broadway"]

for i in a:
    if isinstance(i,str):
        print(i)