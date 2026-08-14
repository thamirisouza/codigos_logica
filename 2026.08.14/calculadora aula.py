import os


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def somar():
    cls()
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 + n2)

    input("Tecle [Enter] para continuar...")
    main()


def diminuir():
    cls()
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 - n2)

    input("Tecle [Enter] para continuar...")
    main()    


def multiplicar():
    cls()
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 * n2)

    input("Tecle [Enter] para continuar...")
    main()


def dividir():
    cls()
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    print("Resultado:", n1 / n2)

    if n2 == 0:
        print("\nERRO: Não é possível dividir por zero!")
    else:
        print("Resultado:", n1 / n2)

    input("Tecle [Enter] para continuar...")

    main()


def main(error=str()):
    # Programa principal e "main loop"
    while True:
        # Limpa a tela
        cls()

        # Cabeçalho
        print("[ VAMOS CALCULAR? - MENU PRINCIPAL ]")

        # Exibe menu principal
        print('''
Opções:

1 - Somar
2 - Diminuir
3 - Multiplicar
4 - Dividir
0 - Sair do programa
    ''')

        # Exibe mensagem de error se existir
        if error:
            print("-----", error, "-----")

        # Recebe opção do usuário
        opcao = input("Escolha uma opção: ")

        # Executa a opção selecionada
        match opcao:
            case "1":
                somar()
            case "2":
                diminuir()
            case "3":
                multiplicar()
            case "4":
                dividir()
            case "0":
                # Limpa a tela, exibe confirmação e termina o programa
                cls()
                print("\nAcabou!")
                exit()
            case _:
                # Se escolheu uma opção inválida, chama o menu novamente, mas, com a mensagem de erro.
                error = "Digite uma opção válida!"
                main(error)


# "Roda" o programa
main()
 