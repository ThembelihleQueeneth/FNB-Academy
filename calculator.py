

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

add = num1 + num2
subtract = num1 - num2
multiply = num1*num2


print("\n==============================")
print("      CALCULATOR RESULTS")
print("==============================")
print(f"First Number: {num1}")
print(f"Second Number: {num2}")
print(f"Addition: {(round(add,2))}")
print(f"Subtraction: {(round(subtract,2))}")
print(f"Multiplication: {(round(multiply,2))}")


#Check for division by zero
if num2 == 0:
    print("Division by zero is not allowed.")
    print("Floor Division: Error ! Cannot divide by zero.")
    print("Modulus: Error ! Cannot divide by zero.")
else:
    divide = round(num1 / num2, 2)
    floor_divide = round(num1 // num2, 2)
    modulus = round(num1 % num2, 2)
    print(f"Division: {(round(divide,2))}")
    print(f"Floor Division: {(round(floor_divide,2))}")
    print(f"Modulus: {(round(modulus,2))}")