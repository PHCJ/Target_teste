import os
# função que imprime as opções do menu
def imprimir_menu():
    print("\n\n\n Selecione uma opção do teste:")
    print("1 - Pergunta 2")
    print("2 - Pergunta 3")
    print("3 - Pergunta 4")
    print("4 - Pergunta 5")
    print("5 - Sair")

# loop principal do programa
while True:
    imprimir_menu()
    opcao = input("Digite o número da opção desejada: ")
    os.system("cls | clear")
    if opcao == "1":
        os.system("python atividade2.py")

    elif opcao == "2":
        os.system("python atividade3.py")

    elif opcao == "3":
        os.system("python atividade4.py")

    elif opcao == "4":
        os.system("python atividade5.py")

    elif opcao == "5":
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida. Tente novamente.")