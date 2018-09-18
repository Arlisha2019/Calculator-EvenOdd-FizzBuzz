first_number = int(input("Enter first number: "))
math_operation = input("Enter one of the following(+,-,*,/): ")
second_number = int(input("Enter second number: "))


def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    return first_number / second_number

if(math_operation == "+"):
    result = addition(first_number, second_number)
    print(result)
elif(math_operation == "-"):
    result = substraction(first_number, second_number)
    print(result)
elif(math_operation == "*"):
    result = multiplication(first_number, second_number)
    print(result)
elif(math_operation == "/"):
    result = division(first_number, second_number)
    print(result)
