print("Simple calculator (exit to leave)")

while True:
    try:
        a = input("First number (or exit): ")
        if a.lower() == "exit":
            break

        a = float(a)
        c = input("Type of operation (+, -, *, /, **, % or exit): ").strip()

        if c.lower() == "exit":
            break
        
        b = input("Second number (or exit): ")
        
        if b.lower() == "exit":
            break
        b = float(b)

        if c == '+':
            d = a + b
        elif c == '-':
            d = a - b
        elif c in ('x', '*'):
            d = a * b
        elif c in ('/', '÷'):
            if b == 0:
                print("Error: Division by zero.")
                continue
            d = a / b
        elif c == '**':
            d = a ** b
        elif c == '%':
            d = a % b
        else:
            print("Invalid operation. Try again.")
            continue

        # formatação dinâmica do resultado
        resultado_formatado = f"{d:.2f}" if d % 1 != 0 else f"{int(d)}"
        print(f"Result: {resultado_formatado}")

    except ValueError:
        print("Error: Please use valid numbers.")

print("Calculator closed.")

