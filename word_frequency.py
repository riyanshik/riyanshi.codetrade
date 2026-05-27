# This program counts word frequency

# collections.Counter can count words automatically in one line

from collections import Counter

sentence = "python is easy and python is powerful"

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print("Using normal method:")
print(frequency)

# Using Counter in one line
counter_result = Counter(words)

print("Using Counter:")
print(counter_result)