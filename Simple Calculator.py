import math
from statistics import mode, StatisticsError

def calculator():
    print("Scientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Exponential")
    print("12. Factorial")
    print("13. Absolute Value")
    print("14. Round")
    print("15. Mode")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice not in range(1, 16):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 15.")

    if choice in [1, 2, 3, 4, 5]:
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice == 1:
            print("Result: ", num1 + num2)
        elif choice == 2:
            print("Result: ", num1 - num2)
        elif choice == 3:
            print("Result: ", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print("Result: ", num1 / num2)
            else:
                print("Error: Division by zero is not allowed.")
        elif choice == 5:
            print("Result: ", num1 ** num2)

    elif choice in [6, 7, 8, 9, 10, 11, 12, 13, 14]:
        while True:
            try:
                num = float(input("Enter the number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        if choice == 6:
            if num >= 0:
                print("Result: ", math.sqrt(num))
            else:
                print("Error: Cannot calculate the square root of a negative number.")
        elif choice == 7:
            print("Result: ", math.sin(math.radians(num)))
        elif choice == 8:
            print("Result: ", math.cos(math.radians(num)))
        elif choice == 9:
            print("Result: ", math.tan(math.radians(num)))
        elif choice == 10:
            if num > 0:
                print("Result: ", math.log(num))
            else:
                print("Error: Cannot calculate the logarithm of a non-positive number.")
        elif choice == 11:
            print("Result: ", math.exp(num))
        elif choice == 12:
            if num >= 0 and num == int(num):
                print("Result: ", math.factorial(int(num)))
            else:
                print("Error: Cannot calculate the factorial of a negative or non-integer number.")
        elif choice == 13:
            print("Result: ", abs(num))
        elif choice == 14:
            print("Result: ", round(num))

    elif choice == 15:
        while True:
            try:
                nums = input("Enter a list of numbers separated by space: ")
                nums = list(map(float, nums.split()))
                print("Result: ", mode(nums))
                break
            except ValueError:
                print("Invalid input. Please enter numbers separated by space.")
            except StatisticsError:
                print("Error: No unique mode found.")

calculator()
