import time
menu = '''
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
~                              ~   
~    Escolha uma operação:     ~
~                              ~
~   [d] - Depositar            ~
~   [s] - Sacar                ~
~   [e] - Extrato              ~
~   [q] - Sair                 ~
~                              ~
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
'''


saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print('-'.center(40,'-'))
    opcao = input(menu)
    print('-'.center(40,'-'))

    if opcao.lower() == 'd':
        print('Opção [d] - Depositar')
        print('-'.center(40,'-'))
        print('Digite o valor da quantia que deseja, depositar: ')
        deposito = float(input(''))
        if deposito > 0:
            saldo += deposito
            print('Depósito de R$ {:_.2f} efetuado com sucesso!'.format(deposito).replace('.',',').replace('_','.'))
            extrato += '\n Depósito de R$ {:_.2f} realizado as {}'.format(deposito,time.ctime().replace('_','.'))
            
        else:
            print('Valor inválido.')

    elif opcao.lower() == 's':
        print('Opção [s] - Sacar')
        print('-'.center(40,'-'))
        print('Digite o valor da quantia que deseja, sacar: ')
        saque = int(input())
        if saque < saldo:
            if (numero_saques <= LIMITE_SAQUES) and (saque <= limite):
                saldo -= int(saque)
                numero_saques += 1
                print('Sacando R$ {:_} ...'.format(saque))
                print('Saque efetuado com sucesso. Você possui {} saque(s) disponíveis.'.format(LIMITE_SAQUES - numero_saques))
                extrato +='\n Saque de R$ {:_.2f} realizado as {}'.format(saque,time.ctime().replace('_','.'))
                
            else:
                if numero_saques > LIMITE_SAQUES:
                    print('Limite diário de saque.')
                else:
                    print('Valor do saque maior que o permitido, o valor permitido por saque é de R$ 500,00.')     
        else:
            print('Você não possui saldo suficiente, o seu saldo é de R$ {} reais.'.format(saldo))       

    elif opcao.lower() == 'e':
        print('Opção [e] - Extrato')
        print('-'.center(40,'-'))
        print('Extrato: ')
        print(extrato)
        print('-'.center(40,'-'))
        print('O seu saldo é de: ')
        print('R$ {:_.2f}'.format(saldo).replace('.',',').replace('_','.'))

    elif opcao.lower() == 'q':
        print('Opção [q] - Sair')
        print('-'.center(40,'-'))
        print('Deslogando ...')
        time.sleep(3)
        print('Obrigado por utilizar nosso sistema')
        break

    else:
       print('Operação inválida, por favor selecione novamente a operação desejada.')