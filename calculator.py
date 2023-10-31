# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Function to modulus two numbers
def modulo(x, y):
    return x % y
# Main calculator loop
while True:
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' for Modulus")
    print("Enter '6' to end the program")

    user_input = input("Enter your choice: ")

    if user_input == "quit":
        break

    if user_input in ("1", "2", "3", "4","5"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "1":
            print("Result:", add(num1, num2))
        elif user_input == "2":
            print("Result:", subtract(num1, num2))
        elif user_input == "3":
            print("Result:", multiply(num1, num2))
        elif user_input == "4":
            result = divide(num1, num2)
        elif user_input == "5":
            result = modulo(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:", result)
    else:
        print("Invalid input")