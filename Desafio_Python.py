import locale

# Configura o locale para o Brasil (pt_BR)
locale.setlocale(locale.LC_MONETARY, "pt_BR.UTF-8")

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0
limite = 500
numero_saques = 0
LIMITE_SAQUES = 2
extrato = []  # Lista para armazenar as operações

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Informe o valor a ser depositado: "))
        if deposito > 0:
            extrato.append(("Depósito", deposito))
            saldo += deposito
            print("Valor adicionado com sucesso")
            print(f"Novo saldo: {locale.currency(saldo)}")
        else:
            print("Valor de depósito inválido.")

    elif opcao == "s":
        print("Sacar")
        saque = float(input("Informe o valor que deseja sacar: "))
        if saque > 0:
            if LIMITE_SAQUES >= numero_saques:
                if saque <= saldo:
                    if saque <= limite:
                        extrato.append(("Saque", saque))
                        saldo -= saque
                        numero_saques += 1
                        print("Valor sacado com sucesso")
                        print(f"Novo saldo: {locale.currency(saldo)}")
                    else:
                        print("Valor máximo de saque por operação é de R$ 500,00")
                else:
                    print("Saldo insuficiente para saque")
            else:
                print(
                    "O seu limite é de 3 saques diários, favor procurar a sua agência"
                )
        else:
            print("Valor de saque inválido.")

    elif opcao == "e":
        print("\n******************* EXTRATO ********************")
        if extrato:
            print("Extrato:")
            for operacao, valor in extrato:
                print(f"Tipo: {operacao} + Valor: {locale.currency(valor)}")
            print(f"Saldo atual: {locale.currency(saldo)}")
        else:
            print("Nenhuma operação registrada no extrato.")
        print("**************************************************")
    elif opcao == "q":
        break
    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")
