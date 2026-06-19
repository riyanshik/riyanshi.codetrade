# library_system.py
# This program demonstrates inheritance, method overriding, and polymorphism.
# A base class LibraryItem is extended by Book and EBook classes.
# Each subclass overrides the describe() method to include its own details.

class LibraryItem:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def describe(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year})"


class Book(LibraryItem):
    def __init__(self, title: str, author: str, year: int, pages: int):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self) -> str:
        return (
            f"Book: '{self.title}' by {self.author} "
            f"({self.year}), {self.pages} pages"
        )


class EBook(LibraryItem):
    def __init__(self, title: str, author: str, year: int, file_size_mb: float):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self) -> str:
        return (
            f"EBook: '{self.title}' by {self.author} "
            f"({self.year}), {self.file_size_mb} MB"
        )


# Create Book objects
book1 = Book("The Alchemist", "Paulo Coelho", 1988, 208)
book2 = Book("Atomic Habits", "James Clear", 2018, 320)

# Create EBook objects
ebook1 = EBook("Python Crash Course", "Eric Matthes", 2019, 12.5)
ebook2 = EBook("Deep Learning", "Ian Goodfellow", 2016, 25.8)

# Store all objects in a single list
library_items = [book1, book2, ebook1, ebook2]

# Loop through the list and call describe()
for item in library_items:
    print(item.describe())

# Explore:
# isinstance(book1, LibraryItem) returns True because Book inherits
# from LibraryItem, so every Book object is also considered a LibraryItem.
print("\nIs book1 a LibraryItem?", isinstance(book1, LibraryItem))