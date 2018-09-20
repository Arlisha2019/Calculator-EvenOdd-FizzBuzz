def addition(first_number, second_number):
    return first_number + second_number
def subtraction(first_number, second_number):
    return first_number - second_number
def multiplication(first_number, second_number):
    return first_number * second_number
def division(first_number, second_number):
    return first_number / second_number


def calculate(math_operation, first_number, second_number):
    correct_operator = False

    if(math_operation == "+"):
        correct_operator = True
        result = addition(first_number, second_number)


    if(math_operation == "-"):
        correct_operator = True
        result = substraction(first_number, second_number)


    if(math_operation == "*"):
        correct_operator = True
        result = multiplication(first_number, second_number)


    if(math_operation == "/"):
        correct_operator = True
        result = division(first_number, second_number)


    if(correct_operator == False):
        math_operation = input("Incorrect opertator, please enter one of the following(+,-,*,/): ")
        calculate(math_operation, first_number, second_number)

    else:
        print("Results: ", result)


while True:
    try:

        first_number = int(input("Enter a number: "))
        math_operation = input("Enter one of the following(+,-,*,/): ")
        second_number = int(input("Enter another number: "))

        calculate(math_operation, first_number, second_number)


        play_or_quit = input("Enter 'Q' to quit or 'Y' to play: ")
        play_or_quit = play_or_quit.lower()

        if(play_or_quit == "q"):
            print("*****************************************")
            print("Thank You for playing, see you next time!")
            print("*****************************************")
            break
        else:
            continue
    except ValueError:
        print("Not a valid number!")
