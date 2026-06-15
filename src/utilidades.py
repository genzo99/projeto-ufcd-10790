import os
from datetime import datetime
import shutil

FICHEIRO = "dados.txt"
BACKUP = "dados_backup.txt"
CSV_FICHEIRO = "dados.csv"

CATEGORIAS_DESPESA = [
    "alimentação",
    "transporte",
    "lazer",
    "saúde",
    "educação",
    "serviços",
    "outros"
]

CATEGORIAS_RECEITA = [
    "salário",
    "freelance",
    "investimentos",
    "outros"
]


def garantir_ficheiro():
    if not os.path.exists(FICHEIRO):
        open(FICHEIRO, "w", encoding="utf-8").close()


def backup_dados():
    if os.path.exists(FICHEIRO):
        shutil.copy(FICHEIRO, BACKUP)


def ler_dados():
    garantir_ficheiro()
    movimentos = []
    with open(FICHEIRO, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                tipo, valor, categoria, data, descricao = linha.split(";")
                movimentos.append({
                    "tipo": tipo,
                    "valor": float(valor),
                    "categoria": categoria,
                    "data": data,
                    "descricao": descricao
                })
    return movimentos


def escrever_dados(movimentos):
    backup_dados()
    with open(FICHEIRO, "w", encoding="utf-8") as f:
        for m in movimentos:
            linha = f"{m['tipo']};{m['valor']};{m['categoria']};{m['data']};{m['descricao']}\n"
            f.write(linha)


def validar_valor(mensagem="Valor: "):
    while True:
        valor_str = input(mensagem)
        try:
            valor = float(valor_str)
            if valor <= 0:
                print("O valor deve ser maior que zero.")
            else:
                return valor
        except ValueError:
            print("Valor inválido. Introduza um número.")


def validar_data(mensagem="Data (AAAA-MM-DD): "):
    while True:
        data_str = input(mensagem)
        try:
            datetime.strptime(data_str, "%Y-%m-%d")
            return data_str
        except ValueError:
            print("Data inválida. Use o formato AAAA-MM-DD.")


def escolher_categoria(lista_categorias):
    print("\nCategorias disponíveis:")
    for i, cat in enumerate(lista_categorias, start=1):
        print(f"{i}. {cat}")
    print(f"{len(lista_categorias) + 1}. Outra")

    while True:
        opcao = input("Escolha uma categoria: ")
        try:
            opcao = int(opcao)
            if 1 <= opcao <= len(lista_categorias):
                return lista_categorias[opcao - 1]
            elif opcao == len(lista_categorias) + 1:
                return input("Introduza o nome da categoria: ")
            else:
                print("Opção inválida.")
        except ValueError:
            print("Introduza um número válido.")
