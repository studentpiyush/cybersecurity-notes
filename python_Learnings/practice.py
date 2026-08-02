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