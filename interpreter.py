expression = input("Type a expression: ")
first_number,operator,second_number = expression.split(" ")
x = float(first_number)
z = float(second_number)

if operator == "+":
    print(x+z)
elif operator == "-":
    print(x-z)
elif operator == "*":
    print(x*z)
elif operator == "/":
    print(x/z)