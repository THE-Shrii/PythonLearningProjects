print("It's Calculator that is made by Python basic topics for 2 numbers")
inp1 = int(input("Enter a number: "))
inp2 = int(input("Enter another number: "))

print("Choose operation that you want to perform on this operands")
print("1. Addition : +")
print("2. Subtraction : -")
print("3. Multiplication : *")
print("4. Division : /")

op = int(input("Enter your choice: "))
if op == 1:
    print(inp1 + inp2)
elif op == 2:
    print(inp1 - inp2)
elif op == 3:
    print(inp1 * inp2)
elif op == 4:
    print(inp1 / inp2)
else:
    print("Invalid operation")
