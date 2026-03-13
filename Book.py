class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author

    def display(self):
        print(self.title, self.author)
    def change(self, author):
        self.author=author
b1=Book("Python Basics", "John")
b1.display()
b1.change("David")
b1.display()
