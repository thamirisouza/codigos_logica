############################################
# AGENDA FURRECA.PY                        #
# Versão 2026.08.10                        #
# By Luferat - https://github.xonm/Luferat #
############################################


import subprocess

def cls():
    subprocess.run("cls", shell=True)

def new_contact():
    pass

def list_contacts():
    pass

def edit_contact():
    pass

def delete_contact():
    pass

# Programa principal
def main(erro = str()):
    # Main loop
    while True:
        cls() 
        print("[ AGENDA FURRECA - MENU PRINCIPAL ]")
        print(erro)
        erro = str()
        print('''
Opções:

1 - Novo contato
2 - Listar contatos
3 - Editar contato
4 - Apagar contato
0 - Sair do programa
    ''')
        
        opcao = input("Escolha uma opção: ")

        match int(opcao):
            case 1:
                new_contact()
            case 2:
                list_contacts()
            case 3:
                edit_contact()
            case 4:
                delete_contact()
            case 0:
                cls()
                print("\nAcabou!")
                exit()
            case _:
                erro = "Digite uma opção válida!"
                main(erro)

# "Roda" o programa
main()     