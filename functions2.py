### deep dive in to functions ###
# nested functions # a function within another function

# Basic syntax for nested function
# def outer_function ():
#     def inner_function ():
#         #code
#     return inner_function    

# def outer():
#     def inner():
#         return "This is an inner function!"
#     return inner()
# print(outer())
 
# def process_data(data):
#     def clean(d):
#         return d.strip().lower() ### strip will eliminate the leading and ending spaces and lower will turn to lowercae
#     return[clean(item) for item in data]
# print(process_data([" Hello ", "World "]))

def power_of(n):
    def power(x):
        return x**n
    return power
square_root = power_of(2)
cube_root = power_of(3)

print(square_root(9))
print(cube_root(4))