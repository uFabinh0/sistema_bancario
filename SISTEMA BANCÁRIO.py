menu = """ 

[d] [Depositar]
[s] [Sacar]
[e] [Extrato]
[q] [Sair]

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido")

    elif opcao == "s":
        valor = float(input("Digite o valor a sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente")
        elif excedeu_limite:
            print("Limite excedido")
        elif excedeu_saques:
            print("Limite de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Valor inválido")

    elif opcao == "e":
        print("\n=================== Extrato ===================")
        print("Não foram realizadas transações" if not extrato else extrato)                            
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================================")

    elif opcao == "q":
        break
    else:
        print("Opção inválida")    