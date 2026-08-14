############################################
# 2026.08.14\calculadora.py                #
# CALCULADORA.PY                           #
# Versão 2026.08.14                        #
############################################


def somar():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 + n2)


def dividir():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 / n2)


def multiplicar():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 * n2)


def diminuir():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 - n2)


while True:
    print("=== VAMOS CALCULAR ?===")
    print("1 - Somar")
    print("2 - Dividir")
    print("3 - Multiplicar")
    print("4 - Diminuir")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        somar()

    elif opcao == "2":
        dividir()

    elif opcao == "3":
        multiplicar()

    elif opcao == "4":
        diminuir()

    elif opcao == "5":
        print("Calculadora encerrada!")
        break

    else:
        print("Opção inválida!")

    input("\nPressione ENTER para continuar...")
