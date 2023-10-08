from utils import isfloat

menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == 'd':
        valor = input('Informe o valor do depósito: ')

        if isfloat(valor) and float(valor) > 0:
            valor = float(valor)
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 's':
        valor = input('Informe o valor do saque: ')

        if isfloat(valor) and float(valor) > 0:
            
            valor = float(valor)

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print('Operação falhou! Você não tem saldo suficiente.')
            elif excedeu_limite:
                print('Operação falhou! O valor do saque excede o limite.')
            elif excedeu_saques:
                print('Operação falhou! Número de saques excedido.')
            else:
                saldo -= valor
                extrato += f'Saque: R$ {valor:.2f}\n'
                numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == 'e':
        print(' EXTRATO '.center(50, '='))
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=' * 50)

    elif opcao == 'q':
        break
    
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')
