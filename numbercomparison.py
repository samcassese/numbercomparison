# User types 2 numbers
num1 = float(input("Pick a first number: "))

num2 = float(input("Pick a second number: "))

if num1 > num2:
    print("The first number is greater.")

elif num1 < num2:
    print("The second number is greater.")

elif num1 == num2:
    print("Both numbers equal the same amount.")

else:
    print("Error. Please try running the program again.")