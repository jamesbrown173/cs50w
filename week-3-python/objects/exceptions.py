import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Value Error")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print(f"Error: Cannot divide {x} by {y}")
    sys.exit(1)


print(f"{x} / {y} = {result}")
