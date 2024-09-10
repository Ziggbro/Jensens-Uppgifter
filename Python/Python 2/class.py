# class Book:
#     def __init__(self, title, author, year):

#         self.title = title
#         self.author = author
#         self.year = year
        
#     def describe(self):
#         return f"{self.title}, by {self.author}, published in {self.year}"
    

# book1 = Book("The Stockholm City", "Pierre G", "2018")
# print(book1.title)
# print(book1.describe())



# class Customer():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def hello(self):
#         return f"hej och välkommen {self.name}, {self.age}"


# costumer1 = Customer("alice", "400")

# print(costumer1.hello())




class Car:
    def __init__(self, brand, model, year, speed=0.0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0.0

    def drive(self, input_speed):
        self.speed = input_speed
    
    def stop(self):
        self.speed = 0.0
    
bil1 = Car("Toyota","Corolla","2022","0.0\n")
bil2 = Car("Honda","Civic","2021","0.0\n")

bil1.drive(50)
print("car 1 speed:", bil1.speed)
bil2.drive(70)
print("car 2 speed:", bil2.speed)

bil1.stop()
print("car 1 speedint", bil1.speed)
print("car 2 spdeedent", bil2.speed)

