from operacoes import(adicao, subtracao, multiplicacao, divisao, potencia)


def menu():
    while True:
        print('Calculadora')
        print('Digite 1 para somar')
        print('Digite 2 para subtrair')
        print('Digite 3 para multiplicar')
        print('Digite 4 para dividir')
        print('Digite 5 para potencia')
        print('Digite 6 para sair')
        escolha = int(input('Digite a opcao desejada: '))

        if escolha == 1:
            print(adicao())

        elif escolha == 2:
            print(subtracao())

        elif escolha == 3:
            print(multiplicacao())

        elif escolha == 4:
            print(divisao())

        elif escolha == 5:
            print(potencia())

        elif escolha == 6:
            print('Fim do programa')
            break

menu()
         


    
