total_amount = float(input("Enter total amount: "))
tip_amount = float(input("Enter tip amount in percentage: "))

def grand_total(total_amount, tip_amount):
    total =  total_amount + total_amount * tip_amount/100
    return total

output = grand_total(total_amount, tip_amount)
print("Your total with the tip is {0}".format(output))
