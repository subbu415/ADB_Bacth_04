student = {
    "100": {"name": "supreeth", "English": 75, "Telugu": 85}, 
    "200": {"name": "preeth", "English": 77, "Telugu": 82},
    "300": ["mango"]
}

#print(student)

fruits = ["mango","grapes",["carrot","Orange"],{"name":"Supreeth"}]
#print(fruits)           
#print(student["100"]["name"])
#print(student["name","100"])

#fruits = ("mango","Apple","Guava")
#print(fruits)
#-------------------------------------------------------------------------
#---Indexing
#----1.list
numbers = [10,20,30,40,50,60,70,80,90,100]
print(numbers)
print(numbers[0])
print(numbers[0:6:3]) 
print(numbers[0:6:2])
print(numbers[0:6]) 
print(numbers[0:5:2])
print(numbers[0:5:3])
print(numbers[0:7:2])
name = "Supreeth"
print(name)
print(name[0:5])
print(name[0:6:2])
print(name[-1:-5:-2])
print(numbers[-1:-6:-3])
print(numbers[-1:-5:-2])
print(numbers[::-1])
print(name[::-1])
print(numbers[0:3],numbers[-1:-4:-1])
print(numbers[0:3]+numbers[-1:-4:-1])

#Tuple
numbers=(10,20,30,40,50,60,70,80,90,100)
print(numbers[0:5])
#set
my_set = {10,20,30,40,50,60,70,80,90,100,10,100}
print(my_set)
#print(my_set[0])
#indexing wont work on set
#tuple
my_dict = {'a':100,'b':200,'c':300}
print(my_dict)
print(my_dict['a'])
#print(my_dict[0])
#in dictionary key value works but indexing wont work
#list methods
numbers= [10,20,30,40,50,60,70,80,90,100]
print(numbers)
numbers.append(200)
print(numbers)
numbers.insert(1,300)
print(numbers)
numbers.remove(40)
print(numbers)
numbers.pop()
print(numbers)
print(numbers.index(70))
numbers = (10,20,30,40,50,60,70,80,90,100,100,100)
print(numbers)
print(numbers.count(100))
print(numbers.index(50))
my_set.add(300)
print(my_set)
my_dict['d'] = 400
print(my_dict)
my_dict.pop('b')
print(my_dict) 
