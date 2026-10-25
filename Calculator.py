#

while True:
    print("\n--- Arithmetic Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '6':
        print("Calculator closed!")
        break

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice!")
        continue

    numbers = list(map(float, input(
        "Enter multiple numbers separated by spaces: "
    ).split()))

    if len(numbers) == 0:
        print("Please enter some numbers!")
        continue

    result = numbers[0]

    if choice == '1':
        result = sum(numbers)
        print("Addition =", result)

    elif choice == '2':
        for n in numbers[1:]:
            result -= n
        print("Subtraction =", result)

    elif choice == '3':
        for n in numbers[1:]:
            result *= n
        print("Multiplication =", result)

    elif choice == '4':
        for n in numbers[1:]:
            if n == 0:
                print("Error: Division by zero!")
                break
            result /= n
        else:
            print("Division =", result)

    elif choice == '5':
        for n in numbers[1:]:
            if n == 0:
                print("Error: Modulus by zero!")
                break
            result %= n
        else:
            print("Modulus =", result)
