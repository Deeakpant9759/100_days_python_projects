class QuadraticEquations:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def validation(self):
        if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(self.c, (int, float)):
            raise TypeError("Coefficients must be integers or floats.")

    def calculation(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Infinite solutions"
                else:
                    return "No solution"
            else:
                root = -self.c / self.b
                return (root, )

        discriminant = self.b**2 - 4*self.a*self.c
        if discriminant < 0:
            return "No real roots"
        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            return (root, )
        else:
            root1 = (-self.b + (discriminant)**0.5) / (2 * self.a)
            root2 = (-self.b - (discriminant)**0.5) / (2 * self.a)
            return root1, root2

def main():
    print("-------Welcome to Quadratic Equation Solver-------")
    a = input("Enter coefficient a: ")
    b = input("Enter coefficient b: ")
    c = input("Enter coefficient c: ")
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print("Please enter valid numbers for coefficients.")
        return  # exit if invalid input

    print(f"Your Quadratic Equation is: {a}x\u00B2 + {b}x + {c}")
    equation = QuadraticEquations(a, b, c)
    try:
        equation.validation()
        roots = equation.calculation()
        if isinstance(roots, str):
            print(roots)
        elif len(roots) == 1:
            print(f"The root of the equation is: {roots[0]}")
        else:
            print(f"The roots of the equation are: {roots[0]} and {roots[1]}")
    except Exception as e:
        print("Error:", e)

def Program_running():
    i = 0
    while True:
        cont = input("\nTo Run this Program Type Yes or No: ").strip().lower()
        if cont == 'yes':
            main()
        elif cont == 'no':
            print("Exiting the program.")
            break
        else:
           print("Invalid input. Please type 'Yes' or 'No'.")
           print("You have", 3 - i, "attempts left.")
           if i >= 3:
               print("Too many invalid attempts. Exiting the program.")
               break
        i += 1
if __name__ == "__main__":
    Program_running()
