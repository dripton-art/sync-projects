# Simple calculator
a = int(input("enter 1st number. "))
b = int(input("enter 2nd number. "))

Add = a + b
Subtract = a - b
Multiply = a * b

print(f"a + b = {Add:.1f}")
print(f"a - b = {Subtract:.1f}")
print(f"a * b = {Multiply:.1f}")

if b == 0:
    print("\n*cannot be divided by zero*")
else:
    Divide = a / b
    print(f"a / b = {Divide:.1f}")