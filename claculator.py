
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

power = lambda x, y: x ** y

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

while True:
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Factorial")
    print("7. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        if choice == '1':
            result = add(num1, num2)
            operation = "addition"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "subtraction"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "multiplication"
        elif choice == '4':
            result = divide(num1, num2)
            operation = "division"
        elif choice == '5':
            result = power(num1, num2)
            operation = "exponentiation"
        
        print(f"The result of {num1} {operation} {num2} is {result}")
    
    elif choice == '6':
        num = int(input("Enter a non-negative integer: "))
        result = factorial_recursive(num)
        print(f"The factorial of {num} is {result}")
    
    elif choice == '7':
        print("Exiting the calculator.")
        break
    
    else:
        print("Invalid choice. Please choose a valid operation.")
