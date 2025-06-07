# # # loops
# # # 1.for loops
# # # 2.while loops
# # li = (1,2,3,4,5)
# # for i in li:
# #     # print(i)
# #     print(i,"iteration")
# li = ["orange","apple","grapes"]
# for i in li:
#     print(i,"iterate")

# range() -> create sequence of numbers to iter
# for i in range(1,11,1):
#     print(i)
# for i in range (1,11,3):
#     print(i)
# for i  in range (11):
#     print(i)
# for ch in "supreeth":
#     print(ch)
# name = input("enter the name:")
# # find the no.of vowels in the name
# vowels = ['a','e','i','o','u']
# vowel_count = 0
# for ch in name:
#     if ch in vowels:
#         vowel_count=vowel_count+1
        
# print(vowel_count)  

# name = input("enter the name:")
# # find the no.of vowels in the name
# vowels = ['a','e','i','o','u']
# vowel_count = 0
# for ch in name:
#     if ch in vowels:
#         vowel_count=vowel_count+1
        
# print("There are", vowel_count, "vowels in",name)  

# while loop = it will execute the block of code repeatedly as long as the condition is true

# c=0
# while c <= 5:
#     print(c)
#     c+=1

# while True:
#     resp = input("type 'exit' to stop:")
#     if resp == "exit":
#         break
#     else:
#         print("your response is",resp)

# for i in range (1,6):
#     if i == 3:
#         continue
#     else:
#         print(i)

# for i in range (1,6):
#     if i == 3:
#         break
#     else:
#         print(i)

# for i in range (1,11):
#     print("2*",i,"=",2*i)

# for i in range (1,11):
#     print("2 *",i,"=",2*i)

# String formaters
# 1. .format()
# for i in range (1,11):
#     print("2 * {0} = {1}".format(i,2*i))

# for i in range (1,11):
#     print("2 * {iter} = {mul}".format(iter=i,mul=2*i))

# 2. f"" --- short hand notation
# for i in range (1,11):
#     print(f"2 * {i} = {2*i}")

# nested loops
#-----------------------------------------
# for i in range (2,6):
#     for j in range (1,11):
#         print(f"{i} * {j} = {i*j}")
# print("--------------------------")

#  printing only even number multiplications
# for i in range (2,11,2):
#     for j in range (1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("--------------------------")

# printing only odd number multiplication
# for i in range (1,12,2):
#     for j in range (1,11):
#         print(f"{i} * {j} = {i*j}")
#     print("--------------------------")

### Half pyramid ###
# for i in range (1,7):
#     print(i*"*")

### Inverted Half Pyramid ###
# for i in range (6,0,-1):
#     print (i*"*")

# def full_pyramid(n):
#     for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print(" ", end="")
        
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()
   
# full_pyramid(5)


    
















