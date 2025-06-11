### A function is a reusable block of code that performs a specific task ###
### def is a keyword to define function ###
# def greet():
#     return "Hello World"
# print(greet())

# def addition(a,b):
#     return a+b
# print (addition(10,20))
# print (addition(100,135))

def square (n):
    return n**2
#print(square(4))
# def addition (a,b,c=0):
#     return a+b+c
# print (addition(10,20))
# print (addition(25,36,18))

### args is used when there is n no.of values ### it will be of type tuple
# def addition (*args):
#     return sum(args)
# print(addition(15,25,68,9,37,18))

### kwargs will be of dictonary type
# def print_info(**kwargs):
#     for key,value in kwargs.items():
#         print(key,value)

# print(print_info(name ="Jagadesh",age=35,occupation="tech"))      

### Variable Scope

# x =10  # Global Variable
# def some ():
#     x = 5 # local variable
#     return x
# print (some()) 
#  
x =10  # Global Variable
def some ():
    x = 5 # local variable
    return x
print(x)
print (some()) 
