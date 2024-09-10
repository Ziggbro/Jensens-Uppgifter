class Book:
    def __init__(self, title, author, year):

        self.title = title
        self.author = author
        self.year = year
        
    def describe(self):
        return f"{self.title}, by {self.author}, published in {self.year}"
    

book1 = Book("The Stockholm City", "Pierre G", "2018")
print(book1.title)
print(book1.describe())