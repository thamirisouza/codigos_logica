def calculadora():
    print("=== CALCULADORA ===")

    numero1 = float(input("Primeiro número: "))
    operacao = input("Operação (+, -, *, /): ")
    numero2 = float(input("Segundo número: "))

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "*":
        resultado = numero1 * numero2
    elif operacao == "/":
        resultado = numero1 / numero2
    else:
        print("Operação inválida.")
        return

    print("Resultado:", resultado)


calculadora()