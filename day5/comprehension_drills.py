# comprehension_drills.py
# This program demonstrates the use of list comprehensions in Python.
# It solves four problems using list comprehensions without traditional for loops.
# It also includes examples of dictionary and set comprehensions.

# 1. Extract numbers divisible by 3 from a list of 20 integers
numbers = list(range(1, 21))
div_by_3 = [num for num in numbers if num % 3 == 0]

# 2. Return words longer than 4 characters in title case
words = ["apple", "cat", "banana", "dog", "elephant", "fish"]
long_words = [word.title() for word in words if len(word) > 4]

# 3. Convert temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

# 4. Flatten a nested list using a single comprehension
nested_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
flattened = [num for sublist in nested_list for num in sublist]

# Explore: Dictionary comprehension example
square_dict = {num: num ** 2 for num in range(1, 6)}

# Explore: Set comprehension example
square_set = {num ** 2 for num in range(1, 6)}

# Print results
print("Numbers divisible by 3:", div_by_3)
print("Words longer than 4 characters in title case:", long_words)
print("Temperatures in Fahrenheit:", fahrenheit)
print("Flattened list:", flattened)
print("Dictionary comprehension example:", square_dict)
print("Set comprehension example:", square_set)