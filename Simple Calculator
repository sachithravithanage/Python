class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        return a / b

    def modulus(self, a, b):
        if b == 0:
            return "Error! Modulus by zero."
        return a % b

    def power(self, a, b):
        # manual exponentiation
        result = 1
        negative = False
        if b < 0:
            b = -b
            negative = True
        for _ in range(b):
            result *= a
        return 1 / result if negative else result

    def factorial(self, n):
        if n < 0:
            return "Error! Factorial of negative."
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def floor_division(self, a, b):
        if b == 0:
            return "Error! Division by zero."
        q = a / b
        if q >= 0:
            return int(q)  # truncation works for positive
        else:
            return int(q) - (1 if q != int(q) else 0)  # adjust for negatives


def main():
    calc = Calculator()
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Power (a^b)")
        print("7. Factorial")
        print("8. Floor Division")
        print("9. Exit")

        choice = input("Enter choice (1-9): ")

        if choice == '9':
            print("Exiting calculator.")
            break

        if choice == '7':  # factorial takes single number
            n = int(input("Enter number: "))
            print("Result:", calc.factorial(n))
        else:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", calc.add(a, b))
            elif choice == '2':
                print("Result:", calc.subtract(a, b))
            elif choice == '3':
                print("Result:", calc.multiply(a, b))
            elif choice == '4':
                print("Result:", calc.divide(a, b))
            elif choice == '5':
                print("Result:", calc.modulus(a, b))
            elif choice == '6':
                print("Result:", calc.power(a, int(b)))
            elif choice == '8':
                print("Result:", calc.floor_division(a, b))
            else:
                print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
