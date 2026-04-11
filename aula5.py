# Revisão if e else

# idade = int(input('Digite sua idade: '))

# if idade >= 18:
#     print('É maior de idade')
# else:
#     print('Não é maior de idade')

# numero = int(input('Digite um número: '))

# if numero % 2 == 0:
#     print('O número é par')
# else:
#     print('O número é ímpar')

# nota1 = float(input('Digite sua primeira nota: '))
# nota2 = float(input('Digite sua segunda nota: '))
# nota3 = float(input('Digite sua terceira nota: '))

# media = (nota1 + nota2 + nota3)/3

# print(media)

# if media >= 7:
#     print('Aprovado')
# else:
#     print('Recuperação')


# produto = float(input('Digite o preço do produto: '))

# if produto >= 100:
#     print('O produto é caro')
# else:
#     print('O produto é barato')

# numero = int(input('Digite um número: '))

# if numero > 0:
#     print('Esse número é positivo')
# else:
#     print('Esse número é negativo')


# saldo = 1000

# opcao = int(input('1 - Consultar saldo\n2 - Sacar\n3 - Depositar\nResposta: '))


# if opcao == 1:
#     print(f'Saldo atual = {saldo}')
# elif opcao == 2:
#     saque = float(input('Quanto você deseja sacar? '))
#     if saque > saldo:
#         print('Saldo insuficiente')
#     else:
#         saldo = saldo - saque
#         print(f'Saque realizado com sucesso!\nSaldo atual = {saldo}')
# elif opcao == 3:
#     deposito = float(input('Quanto você deseja depositar? '))
#     saldo = saldo + deposito 
#     print(f'Deposito realizado com sucesso!\nValor atual = {saldo}')
# else:
#     print('Opção inválida')


# menu = int(input('1 - Criar conta\n2 - Fazer login\n3 - Recuperar senha\nResposta: '))

# if menu == 1:
#     nome = input('Digite seu nome: ')
#     email = input('Digite seu email: ')
#     senha = int(input('Digite sua senha: '))
#     print(f'Conta criada com sucesso para {nome}')
# elif menu == 2:
#     email = input('Digite seu email: ')
#     senha = int(input('Digite sua senha: '))
#     print("Login realizado com sucesso!")
# elif menu == 3:
#     email = input('Digite seu email: ')
#     print('Deseja receber o código por email ou SMS?')
#     codigo = input()
#     print("Instruções enviadas")
# else:
#     print('invalido')

# opcao = ''

# while(opcao != 3):
#     opcao = int(input('1 - Cadastrar usuário\n2 - Listar usuários\n3 - Sair do sistema\nResposta: '))
#     if opcao == 1:
#         nome = input('Digite o nome: ')
#         telefone = input('Digite seu telefone: ')
#         print('Cadastro realizado com sucesso!')
#     elif opcao == 2:
#         print('Maria - 859999999\nJoão - 856666666')
#     elif opcao == 3:
#         print('Saindo...')
#     else:
#         print('Opção inválida')

# saldo = 1000

# opcao = ''

# while(opcao != 4):
#     opcao = int(input('1 - Consultar saldo\n2 - Sacar\n3 - Depositar\n4 - Sair do sistema\nResposta: '))
#     if opcao == 1:
#         print(f'Saldo atual = {saldo}')
#     elif opcao == 2:
#         saque = float(input('Quanto você deseja sacar? '))
#         if saque > saldo:
#             print('Saldo insuficiente')
#         else:
#             saldo = saldo - saque
#             print(f'Saque realizado com sucesso!\nSaldo atual = {saldo}')
#     elif opcao == 3:
#         deposito = float(input('Quanto você deseja depositar? '))
#         saldo = saldo + deposito 
#         print(f'Deposito realizado com sucesso!\nValor atual = {saldo}')
#     elif opcao == 4:
#         print('Saindo...')
#     else:
#         print('Opção inválida')


# Atv com for i in range

# for i in range (3):
#     desejo = input(f'Desejo {i+1} ')

# compra = float(input('Digite o valor da compra: '))
# parcelas = int(input('Digite quantas parcelas deseja: '))

# while not (parcelas > 0 and parcelas <= 12):
#     parcelas = int(input('Número inválido, selecione entre 1 e 12 parcelas\nDigite quantas parcelas deseja: '))

# valorParcela = compra/parcelas

# for i in range (parcelas):
#     print(f'Parcela {i+1} = {valorParcela}')


# numero = int(input('Digite um número: '))

# for i in range (10):
#     print(f'A tabuada do {numero} é: {numero} x {i+1} = {numero * (i+1)}')

# Revisão Lista

# lista.append (item) -> adiciona um elemento no final da lista
# lista.insert (posição,item) -> adiciona um elemento numa posição específica
# lista.pop() -> Remove o último elemento da lista
# lista.pop(posição) -> Remove um elemento de uma posição específica
# lista.index(item) -> A posição em que o item está

# produtos = ['notebook', 'Tablet', 'Mouse']
# produtos.append('Carregador')
# produtos.insert(0,'fone')
# produtos.pop()
# produtos.pop(1)
# produtos.index('mouse')

# produtos = ['Notebook', 'Tablet', 'Mouse']

# opcao = ''

# while (opcao != 3):
#     opcao = int(input('1 - Adicionar produtos ao carrinho\n2 - Listar os produtos\n3 - Sair\nResposta: '))
#     if opcao == 1:
#         produto = input('Nome do produto: ')
#         produtos.append(produto)
#     elif opcao == 2:
#         for produto in produtos:
#             print(produto)
#     elif opcao == 3:
#         print('Saindo...')

