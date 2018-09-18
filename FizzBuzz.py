

number_input = int(input("Please enter a whole number: "))

def is_divisible():
    if(number_input % 3 == 0 and number_input % 5 == 0):
        print("Fizz Buzz")
    elif(number_input % 3 == 0):
        print("Fizz")
    elif(number_input % 5 == 0):
        print("Buzz")

is_divisible()
