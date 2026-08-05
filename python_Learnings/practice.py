ports = [22, 80, 443, 8080]
usernames = ["admin","root","guest"]
mixed = ["server1", 443, True]

print(ports[0])
print(ports[-1])
print(ports[1:3])

ports[0] = 2222
print(ports)

common_password = ["123456", "password", "admin", "letmein"]

if "123456" in common_password:
    print("This password is in the common list.")



services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MYSQL"
}

print(services[22])
print(services[443])

services[8080] = "HTTP-ALT"



del services[3306]

print(services)

if 22 in services:
    print(f"Port 22 runs {services[22]}")

result = services.get(9999, "Unknown")
print(result)    

print("Here", 2 ** 10)

def greet(name):
    print(f"Hello, {name}. Welcome to the system.")

name = input("What is you name : ")

greet(name)

def check_length(password, min_length):
    if len(password) >= min_length:
        return True
    else:
        return False

result = check_length("TR0ub4dor", 8)
print(result)

print("<====Simple Calculator====>")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

while True:
    print("Available Operation :- ")

    print("1. + ")
    print("2. - ")
    print("3. * ")
    print("4. / ")
    print("5. exit")

    Choice = input("Choose an Operation from the list given above : ")

    if Choice == "1":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = add(a, b)
        print(result)
    elif Choice == "2":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = subtract(a,b)
        print(result)
    elif Choice == "3":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = multiply(a,b)
        print(result)
    elif Choice == "4":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        result = divide(a,b)
        print(result)
    elif Choice == "5":
        print("Thank you for visiting,Come again!")
        break;

    else:
        print("Invalid option. Please choose from 1 to 5.")