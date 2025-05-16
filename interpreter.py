def main():
    expression = input("Enter an arithemetic expression: ")
    x, y, z = expression.split(" ")
    if y == "+":
        print(float(int(x) + int(z)))
    elif y == "-":
        print(float(int(x) - int(z)))
    elif y == "*":
        print(float(int(x) * int(z)))
    elif y == "/":
        print(float(int(x) / int(z)))

main()
