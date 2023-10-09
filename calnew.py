import math

print("-------------Welcome to my calculator------------")
print("                Select Operation                ")
print("1  Add")
print("2  Subtract")
print("3  Multiply")
print("4  Divide")
print("5  Square Root")
print("6  Sine")
print("7  Cosine")
print("8  Tangent")
print("9  Cotangent")
print("10 Factorial")

choice = input("Please enter 1/2/3/4/5/6/7/8/9/10 for the operation: ")

if choice in ("1", "2", "3", "4"):
    number1 = float(input("Please enter the first number: "))
    number2 = float(input("Please enter the second number: "))
    
    if choice == "1":
        print("Result:", number1 + number2)
    elif choice == "2":
        print("Result:", number1 - number2)
    elif choice == "3":
        print("Result:", number1 * number2)
    elif choice == "4":
        if number2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", number1 / number2)
elif choice in ("5", "6", "7", "8", "9", "10"):
    number3 = float(input("Please enter a number: "))
    
    if choice == "5":
        if number3 < 0:
            print("Please enter a valid number again.")
        else:
            print("Result:", math.sqrt(number3))
    elif choice == "6":
        print("Result:", math.sin(math.radians(number3)))
    elif choice == "7":
        print("Result:", math.cos(math.radians(number3)))
    elif choice == "8":
        print("Result:", math.tan(math.radians(number3)))
    elif choice == "9":
        cotangent = 1 / math.tan(math.radians(number3))
        print("Result:", cotangent)
    elif choice == "10":
        if number3 < 0:
            print("Invalid number!!!")
        elif number3 == 0:
            print("Result: 1")
        else:
            result = 1
            for i in range(1, int(number3) + 1):
                result *= i
            print("Result:", result)
else:
    print("Invalid input")