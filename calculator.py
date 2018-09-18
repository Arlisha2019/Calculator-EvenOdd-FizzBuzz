first_number = int(input("Enter first number: "))
math_operation = input("Enter one of the following(+,-,*,/): ")
second_number = int(input("Enter second number: "))

def calculator():
    if(math_operation == '+'):
        print(first_number + second_number)
    elif(math_operation == "-"):
        print(first_number - second_number)
    elif(math_operation == '*'):
        print(first_number * second_number)
    elif(math_operation == '/'):
        print(first_number / second_number)
    else:
        print("Invaild Entry")

calculator()
