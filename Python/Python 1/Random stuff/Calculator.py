

operator = input("enter modifer")

num1 = float(input("enter the first number"))
num2 = float(input("enter the seccond number"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result num1 * num2
elif operator == "/":
    result num1 / num2
else:
    print("error")

print(result)