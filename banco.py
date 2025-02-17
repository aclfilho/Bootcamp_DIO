menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

'''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
limite_saques = 3

while True:
    
    opcao = input(menu)
    
    if opcao == 'd':
        print('Deposite')
        
    if opcao == 's':
        print('Saque')
    
    if opcao == 'e':
        print('Extrato')
        
    if opcao == 'q':
        print('Sair')
        

    else:
        print("Operação inválida, selecione uma operação válida")
    