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




class Car():
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def drive(self):
        return f"Bil {self.brand}, {self.model},{self.year},{self.speed}"

bil1 = Car("Toyota","Corolla","2022","0.0\n")
bil2 = Car("Honda","Civic","2021","0.0\n")

print(bil1.drive(),bil2.drive())

