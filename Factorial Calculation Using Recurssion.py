
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

try:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Invalid input! Enter a non-negative number.")
    else:
        print("Factorial =", factorial(num))

except ValueError:
    print("Invalid input! Please enter an integer.")
