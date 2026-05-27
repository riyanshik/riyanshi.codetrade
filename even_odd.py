# This program checks whether a number is even, odd, or zero

# int("abc") gives an error because "abc" is not a valid number

try:

    number = int(input("Enter number: "))

    if number == 0:
        print("Zero")

    elif number % 2 == 0:
        print("Even")

    else:
        print("Odd")

except:
    print("Please enter a valid number")