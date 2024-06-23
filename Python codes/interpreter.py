def main():
    
    expression = input("Expression: ").strip()
    parts = expression.split()
    if len(parts) != 3:
        print("Invalid input format. Ensure the input is in the form 'x y z'.")
        return

    try:
        x = int(parts[0])
        operator = parts[1]
        z = int(parts[2])
    except ValueError:
        print("Invalid input. Ensure x and z are integers.")
        return

    if operator == '+':
        result = x + z
    elif operator == '-':
        result = x - z
    elif operator == '*':
        result = x * z
    elif operator == '/':
        if z == 0:
            print("Division by zero is not allowed.")
            return
        result = x / z
    else:
        print("Invalid operator")
        return

    result = float(result)
    print(f"{result:.1f}")

main()
