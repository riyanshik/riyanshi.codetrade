# This program calculates tip

# return sends a value back from a function
# print only shows the output on the screen

def calculate_tip(bill, tip_percent):

    tip = bill * tip_percent / 100
    total = bill + tip

    return {
        "tip": tip,
        "total": total
    }

result1 = calculate_tip(1000, 10)
result2 = calculate_tip(500, 5)
result3 = calculate_tip(2000, 18)

print(result1)
print(result2)
print(result3)