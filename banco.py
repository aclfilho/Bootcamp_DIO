def depositar(saldo, extrato):
    """Função para realizar um depósito"""
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! Tente novamente com outro valor.")

    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite, limite_saques):
    """Função para realizar um saque"""
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente.")

    elif excedeu_limite:
        print("O valor do saque excede o limite permitido.")

    elif excedeu_saques:
        print("Você já atingiu o limite de saques diários.")

    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

    else:
        print("Operação falhou! Informe um valor válido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    """Função para exibir o extrato"""
    print("\n========== EXTRATO ==========")
    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=============================")


def main():
    """Função principal que executa o menu do sistema"""
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    limite_saques = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """

    while True:
        opcao = input(menu).strip().lower()

        if opcao == 'd':
            saldo, extrato = depositar(saldo, extrato)

        elif opcao == 's':
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite, limite_saques)

        elif opcao == 'e':
            exibir_extrato(saldo, extrato)

        elif opcao == 'q':
            print("Saindo... Obrigado por utilizar nosso sistema!")
            break

        else:
            print("Operação inválida! Tente novamente.")


if __name__ == "__main__":
    main()
