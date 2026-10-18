menu = {
    "1": "Decimal to Binary",
    "2": "Decimal to Octal",
    "3": "Decimal to Hexadecimal",
    "4": "Binary to Decimal",
    "5": "Octal to Decimal",
    "6": "Hexadecimal to Decimal",
    "7": "View History",
    "8": "Exit"
}

for key, value in menu.items():
    print(key, value)

choice = input("Enter your choice: ")

while choice not in menu:
    print("Invalid choice")
    choice = input("Enter your choice: ")

if choice == "1":
    decimal_number = int(input("Enter a decimal number: "))
    binary_number = bin(decimal_number)[2:]
    print(f"Binary representation: {binary_number}")
elif choice == "2":
    decimal_number = int(input("Enter a decimal number: "))
    octal_number = oct(decimal_number)[2:]
    print(f"Octal representation: {octal_number}")
elif choice == "3":
    decimal_number = int(input("Enter a decimal number: "))
    hexadecimal_number = hex(decimal_number)[2:].upper()
    print(f"Hexadecimal representation: {hexadecimal_number}")  