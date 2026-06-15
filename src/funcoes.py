from utilidades import (
    ler_dados,
    escrever_dados,
    validar_valor,
    validar_data,
    escolher_categoria,
    CATEGORIAS_DESPESA,
    CATEGORIAS_RECEITA,
    CSV_FICHEIRO
)


def registar_despesa():
    movimentos = ler_dados()

    print("\n--- Registar Despesa ---")
    valor = validar_valor("Valor da despesa: ")
    categoria = escolher_categoria(CATEGORIAS_DESPESA)
    data = validar_data()
    descricao = input("Descrição: ")

    novo = {
        "tipo": "despesa",
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "descricao": descricao
    }

    movimentos.append(novo)
    escrever_dados(movimentos)

    print("Despesa registada com sucesso!")


def registar_receita():
    movimentos = ler_dados()

    print("\n--- Registar Receita ---")
    valor = validar_valor("Valor da receita: ")
    categoria = escolher_categoria(CATEGORIAS_RECEITA)
    data = validar_data()
    descricao = input("Descrição: ")

    novo = {
        "tipo": "receita",
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "descricao": descricao
    }

    movimentos.append(novo)
    escrever_dados(movimentos)

    print("Receita registada com sucesso!")


def listar_movimentos():
    movimentos = ler_dados()

    print("\n--- Lista de Movimentos ---")
    if not movimentos:
        print("Não existem movimentos registados.")
        return

    for i, m in enumerate(movimentos, start=1):
        print(f"{i}. {m['tipo'].upper()} | {m['valor']:.2f}€ | {m['categoria']} | {m['data']} | {m['descricao']}")


def filtrar_movimentos():
    movimentos = ler_dados()

    print("\n--- Filtrar Movimentos ---")
    print("1. Por tipo (despesa/receita)")
    print("2. Por categoria")
    print("3. Por data")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tipo = input("Tipo (despesa/receita): ").strip().lower()
        filtrados = [m for m in movimentos if m["tipo"] == tipo]

    elif opcao == "2":
        categoria = input("Categoria: ").strip().lower()
        filtrados = [m for m in movimentos if m["categoria"].lower() == categoria]

    elif opcao == "3":
        data = input("Data (AAAA-MM-DD): ").strip()
        filtrados = [m for m in movimentos if m["data"] == data]

    else:
        print("Opção inválida.")
        return

    if not filtrados:
        print("Nenhum movimento encontrado.")
        return

    print("\n--- Resultados do Filtro ---")
    for m in filtrados:
        print(f"{m['tipo'].upper()} | {m['valor']:.2f}€ | {m['categoria']} | {m['data']} | {m['descricao']}")


def calcular_saldo():
    movimentos = ler_dados()

    total_receitas = sum(m["valor"] for m in movimentos if m["tipo"] == "receita")
    total_despesas = sum(m["valor"] for m in movimentos if m["tipo"] == "despesa")

    saldo = total_receitas - total_despesas

    print("\n--- Saldo Total ---")
    print(f"Total de receitas: {total_receitas:.2f}€")
    print(f"Total de despesas: {total_despesas:.2f}€")
    print(f"Saldo final: {saldo:.2f}€")


def resumo_mensal():
    movimentos = ler_dados()
    if not movimentos:
        print("Não existem movimentos registados.")
        return

    ano = input("Ano (AAAA): ")
    mes = input("Mês (MM): ")

    receitas = 0
    despesas = 0

    for m in movimentos:
        if m["data"].startswith(f"{ano}-{mes}"):
            if m["tipo"] == "receita":
                receitas += m["valor"]
            elif m["tipo"] == "despesa":
                despesas += m["valor"]

    saldo = receitas - despesas

    print(f"\n--- Resumo de {ano}-{mes} ---")
    print(f"Receitas: {receitas:.2f}€")
    print(f"Despesas: {despesas:.2f}€")
    print(f"Saldo: {saldo:.2f}€")


def exportar_csv():
    movimentos = ler_dados()
    if not movimentos:
        print("Não existem movimentos para exportar.")
        return

    with open(CSV_FICHEIRO, "w", encoding="utf-8") as f:
        f.write("tipo;valor;categoria;data;descricao\n")
        for m in movimentos:
            linha = f"{m['tipo']};{m['valor']};{m['categoria']};{m['data']};{m['descricao']}\n"
            f.write(linha)

    print(f"Dados exportados para {CSV_FICHEIRO} com sucesso!")


def editar_movimento():
    movimentos = ler_dados()
    if not movimentos:
        print("Não existem movimentos registados.")
        return

    listar_movimentos()

    try:
        indice = int(input("Número do movimento a editar: ")) - 1
        movimento = movimentos[indice]
    except:
        print("Movimento inválido.")
        return

    print("\nDeixe em branco para manter o valor atual.")

    novo_valor = input(f"Valor ({movimento['valor']}): ")
    nova_categoria = input(f"Categoria ({movimento['categoria']}): ")
    nova_data = input(f"Data ({movimento['data']}): ")
    nova_descricao = input(f"Descrição ({movimento['descricao']}): ")

    if novo_valor:
        try:
            movimento["valor"] = float(novo_valor)
        except ValueError:
            print("Valor inválido. Mantido o valor anterior.")
    if nova_categoria:
        movimento["categoria"] = nova_categoria
    if nova_data:
        movimento["data"] = nova_data
    if nova_descricao:
        movimento["descricao"] = nova_descricao

    escrever_dados(movimentos)
    print("Movimento atualizado com sucesso!")


def remover_movimento():
    movimentos = ler_dados()
    if not movimentos:
        print("Não existem movimentos registados.")
        return

    listar_movimentos()

    try:
        indice = int(input("Número do movimento a remover: ")) - 1
        movimentos.pop(indice)
    except:
        print("Movimento inválido.")
        return

    escrever_dados(movimentos)
    print("Movimento removido com sucesso!")
