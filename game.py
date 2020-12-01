import random

nome=str(input('Antes de iniciar, diga seu nome: '))

# Escolha do nível
nivel = int() 
while nivel != 4: # Faz o retorno ao menu

    print("""
        Vamos lá {}! 

        Esse é a +- Matemática -+

        Selecione o nível
        (1) Fácil
        (2) Médio
        (3) Difícil
        (4) Sair
    """.format(nome))

    nivel=int(input(': '))

# Validação do nível
    while nivel not in [1, 2, 3, 4]:
        print('Esse nível não existe, tente novamente!')
        nivel=int(input(': '))

# Entrada nível 1
    if nivel == 1:
        print("""
        (1) Soma
        (2) Subtração
        (3) Retornar ao menu
        """)

        op=int(input(': '))

# Validação do menu nível 1
        while op not in [1, 2, 3]:
            print('Esse modo não existe, tente novamente!')
            op01=int(input(': '))

# Entrada dos modos
        if op == 1: # Modo Soma

            novamente = str()
            while novamente != 'N': # Jogar modo soma novamente

                print('Modo Soma')

                n1=int(random.randint(0, 100))
                n2=int(random.randint(0, 100))

                result=n1+n2

                resultUser=int(input('Quanto é {}+{}? ->'.format(n1, n2)))

# Validação do resultado
            
                if resultUser == result:
                    print('Certo')

                    novamente=input('Quer tentar de novo [S/N]? -> ').upper() # Jogar modo soma novamente

                else:
                    print('Errado')
                    novamente=input('Quer tentar de novo [S/N]? -> ').upper() # Jogar modo soma novamente

        if op == 2: # Modo Subtração
             novamente = str()
             while novamente != 'N': # Jogar modo soma novamente

                print('Modo Subtração')

                n1=int(random.randint(0, 100))
                n2=int(random.randint(0, 100))

                result=n1-n2

                resultUser=int(input('Quanto é {}-{}? ->'.format(n1, n2)))

# Validação do resultado
            
                if resultUser == result:
                    print('Certo')

                    novamente=input('Jogar novamente? [S/N]? -> ').upper() # Jogar modo soma novamente

                else:
                    print('Errado')
                    novamente=input('Jogar novamente? [S/N]? -> ').upper() # Jogar modo soma novamente

        if op == 3: # Sair
            pass

# Entrada nível 2
    if nivel == 2:

        print("""
        (1) Divisão
        (2) Multiplicação
        (3) Retornar ao menu
        """)

        op=int(input(': '))

# Validação do menu nível 2
        while op not in [1, 2, 3]:
            print('Esse modo não existe, tente novamente!')
            op01=int(input(': '))

# Entrada dos modos
        if op == 1: # Modo Divisão

            novamente = str()
            while novamente != 'N': # Jogar modo divisão novamente

                print('Modo Divisão')

#Controle númerico *em processo de criação*

                n1=int(random.randint(1, 20))
                n2=int(random.randint(1, 20))

#//

                result=n1/n2

                resultUser=float(input('Quanto é {}/{}? ->'.format(n1, n2)))

# Validação do resultado
            
                if resultUser == result:
                    print('Certo')

                    novamente=input('Quer tentar de novo [S/N]? -> ').upper() # Jogar modo divisão novamente

                else:
                    print('Errado')
                    novamente=input('Quer tentar de novo [S/N]? -> ').upper() # Jogar modo divisão novamente

        if op == 2: # Modo Multiplicação
             novamente = str()
             while novamente != 'N': # Jogar modo multiplicação novamente

                print('Modo Multiplicação')

                n1=int(random.randint(0, 10))
                n2=int(random.randint(0, 10))

                result=n1*n2

                resultUser=int(input('Quanto é {}*{}? ->'.format(n1, n2)))

# Validação do resultado
            
                if resultUser == result:
                    print('Certo')

                    novamente=input('Jogar novamente? [S/N]? -> ').upper() # Jogar modo multiplicação novamente

                else:
                    print('Errado')
                    novamente=input('Jogar novamente? [S/N]? -> ').upper() # Jogar modo multiplicação novamente

        if op == 3: # Sair
            pass


    if nivel == 3:
        print('Nível indisponível, volte mais tarde')

    if nivel == 4:
        print('\nBye, volte sempre {}!\n'.format(nome))