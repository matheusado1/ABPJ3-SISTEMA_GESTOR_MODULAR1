# Sistema Financeiro Pessoal

receitas = []
despesas = []

def registrar_receita():
    valor = float(input("Digite o valor da receita: "))
    receitas.append(valor)
    print("Receita adicionada com sucesso!")

def registrar_despesa():
    valor = float(input("Digite o valor da despesa: "))
    despesas.append(valor)
    print("Despesa adicionada com sucesso!")

def calcular_saldo():
    total_receitas = sum(receitas)
    total_despesas = sum(despesas)
    saldo = total_receitas - total_despesas
    return saldo

def mostrar_relatorio():
    print("\n RELATÓRIO FINANCEIRO")

    print("\nReceitas registradas:")
    for r in receitas:
        print(f"R$ {r:.2f}")

    print("\nDespesas registradas:")
    for d in despesas:
        print(f"R$ {d:.2f}")

    print("\nTotal de receitas:", sum(receitas))
    print("Total de despesas:", sum(despesas))
    print("Saldo final: R$", calcular_saldo())


while True:
    print("\n MENU FINANCEIRO")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Ver saldo")
    print("4 - Mostrar relatório")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_receita()

    elif opcao == "2":
        registrar_despesa()

    elif opcao == "3":
        saldo = calcular_saldo()
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "4":
        mostrar_relatorio()

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida!")
