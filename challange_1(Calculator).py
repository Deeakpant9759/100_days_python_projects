class Calculator:
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b 

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self.a / self.b

def main():
    print("Welcome to the Calculator Program!")
    print("This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.")
    print("Enter 'q' at any prompt to quit.\n")

    a = input("Enter the first number: ")
    if a.lower() == 'q': return
    b = input("Enter the second number: ")
    if b.lower() == 'q': return

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")    
    print("3. Multiplication")
    print("4. Division")
    
    operation = input("Enter the operation number (1-4): ")
    if operation.lower() == 'q': return

    try:
        operation = int(operation)
        if operation < 1 or operation > 4:
            raise ValueError
    except ValueError:
        print("Invalid operation! Please enter a number between 1 and 4.")
        return

    calc = Calculator(a, b)

    if operation == 1:
        result = calc.add()
        print("Result of addition:", result)
    elif operation == 2:
        result = calc.subtract()
        print("Result of subtraction:", result)
    elif operation == 3:
        result = calc.multiply()
        print("Result of multiplication:", result)
    elif operation == 4:
        try:
            result = calc.divide()
            print("Result of division:", result)
        except ValueError as e:
            print(e)

while True:
    cont = input("enter 'q' to quit or any key to continue: ")
    if cont.lower() == 'q':
        print("Thank you for using the Calculator Program!")
        break
    main()
