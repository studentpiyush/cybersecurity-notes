#calculator program
print("===== Simple Calculator =====")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. +")
print("2. -")
print("3. *")
print("4. %")
print("5. **")

choice = input("Enter your choice (+, -, *, %, **): ")

if choice == "+":
    print("Result:", a + b)

elif choice == "-":
    print("Result:", a - b)

elif choice == "*":
    print("Result:", a * b)

elif choice == "%":
    if b != 0:
        print("Result:", a % b)
    else:
        print("Error: Modulus by zero is not allowed.")

elif choice == "**":
    print("Result:", a ** b)

else:
    print("Invalid operation.")