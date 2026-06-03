from funcoes import *

def menu():
    while True:
        print("\n===================================")
        print("      GESTÃO FINANCEIRA PESSOAL    ")
        print("===================================")
        print("1. Registar despesa")
        print("2. Registar receita")
        print("3. Listar movimentos")
        print("4. Filtrar movimentos")
        print("5. Calcular saldo total")
        print("6. Resumo mensal")
        print("7. Exportar para CSV")
        print("8. Editar movimento")
        print("9. Remover movimento")
        print("0. Sair")
        print("===================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registar_despesa()
        elif opcao == "2":
            registar_receita()
        elif opcao == "3":
            listar_movimentos()
        elif opcao == "4":
            filtrar_movimentos()
        elif opcao == "5":
            calcular_saldo()
        elif opcao == "6":
            resumo_mensal()
        elif opcao == "7":
            exportar_csv()
        elif opcao == "8":
            editar_movimento()
        elif opcao == "9":
            remover_movimento()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
