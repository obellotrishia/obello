class Book:
    def __init__(self, title, author, year_published):
      
       self.title = title
       self.author = author
       self.year_published = year_published

    def describe(self):
      print(f"Title: {self.title}")
      print(f"Author: {self.author}")
      print(f"Year_Published: {self.year_published}")

# Create three book objects
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)
book3 = Book("Pride and Prejudice", "Jane Austen", 1813)

# Display book details
book1.describe()
book3.describe()
book3.describe()