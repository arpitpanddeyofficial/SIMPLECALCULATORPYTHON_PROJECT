import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Modulus by zero"
    return x % y

def square_root(x):
    if x < 0:
        return "Error: Cannot calculate square root of a negative number"
    return math.sqrt(x)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def pi_root(x, root_degree=math.pi):
    if x < 0 and root_degree % 2 == 0: # Even root of negative number
        return "Error: Cannot calculate even root of a negative number"
    return x**(1/root_degree)

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Square Root")
    print("7. Check Prime")
    print("8. Pi-th Root")

    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

        if choice in ('1', '2', '3', '4', '5'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print(f"{num1} % {num2} = {modulus(num1, num2)}")

        elif choice in ('6', '7', '8'):
            try:
                num = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '6':
                print(f"Square root of {num} = {square_root(num)}")
            elif choice == '7':
                if is_prime(int(num)):
                    print(f"{int(num)} is a prime number.")
                else:
                    print(f"{int(num)} is not a prime number.")
            elif choice == '8':
                print(f"Pi-th root of {num} = {pi_root(num)}")

        else:
            print("Invalid input. Please enter a valid choice.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    calculator()
