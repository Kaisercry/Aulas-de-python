# # Revisão aula 8
# # Função sem parâmetro e sem retorno
# # def mandarMensagem():
# #     print('Olá seja bem-vindo ao sistema!')

# # Funções com parâmetro e sem retorno
# #   200 -> Requisição realizada com sucesso
# # # 400 -> Problema no clinte
# # # 500 -> Problema no servidor 
# # def mensageErro(codigo = 200):
# #     if codigo == 200:
# #         print('Requisição realizada com sucesso')
# #     elif codigo == 400:
# #         print('Problema no clinte')
# #     elif codigo == 500:
# #         print('Problema no servidor')
# #     else:
# #         print('Código não reconhecido')

# # # Função com parâmetro e com retorno
# # # imc = peso/altura²
# # def calcularIMC(peso,altura):
# #     imc = peso/(altura*altura)
# #     return imc


# # mandarMensagem()
# # mensageErro(500)
# # print(calcularIMC(80,1.80))
# # print(calcularIMC(altura = 1.80,peso = 80))

# # # Questão 1

# # def mensagemTela():
# #     print('Olá mundo')

# # mensagemTela()

# # # Questão 2

# # def mostrarNome(nome):
# #     print(f'Olá {nome} seja bem-vindo!')

# # mostrarNome('Pietro')


# # # Questão 3

# # def area(altura,base):
# #     areaTerreno = (altura*base)
# #     return areaTerreno

# # print(area(60,35))


# # # Questão 4 

# # def diferenca(numero,numero2):
# #     if numero > numero2:
# #         print(numero2)
# #     elif numero < numero2:
# #         print(numero)
# #     else:
# #         print('Os números são iguais')
    
# # diferenca(25,5)

# # def mostrarNumero(numeral):
# #     if numeral > 0:
# #         print('Esse número é positivo')
# #     else:
# #         print('Esse número é negativo')

# # mostrarNumero(45)
# # mostrarNumero(-45)

# import calculos

# areaQuadrado = calculos.areaQuadrado(3)
# print(f'A área do quadrado é {areaQuadrado}')

# areaT = calculos.areaTriangulo(10,5)
# print(f'A área do triangulo é {areaT}')

# from calculos import areaTrapezio, areaRetangulo

# trapezio = areaTrapezio(10,8,5)
# retangulo = areaRetangulo(3,7)

# print(f'A área do trapezio é {trapezio}')
# print(f'A área do retangulo é {retangulo}')

# from calculos import *

# triangulo = areaTriangulo(3,8)
# print(f'A área do triangulo é {triangulo}')

# import calculos as area

# triangulo = area.areaTriangulo(10,5)
# print(f'A área do triangulo é {triangulo}')

# import alertas as alert

# alertaPagamento = alert.alertaPagamento(True)
# print(alertaPagamento)
# alertaEstoque = alert.alertaEstoque(37)
# print(alertaEstoque)


# import estoque


# opcao = input('1 - Adicionar Produto\n2 - Listar Produto\n3 - Sair\n')

# produtos = [
#     {
#         "nome": "Mouse",
#         "preco": 50,
#         "quantidade": 10
#     },
#     {
#         "nome": "Teclado",
#         "preco": 100,
#         "quantidade": 80
#     }
# ]
# while (opcao != '3'):
#     if opcao == '1':
#         nome = input('Digite o nome do produto: ')
#         preco = float(input('Digite o preço do produto: '))
#         quantidade = int(input('Digite a quantidade do produto: '))
#         estoque.adicionarProduto(produtos, nome, preco ,quantidade)
    
    
#     if opcao == '2':
#         estoque.listarProduto(produtos)
#     opcao = input('1 - Adicionar Produto\n2 - Listar Produto\n3 - Sair\n')



import pyqrcode
import pypng
link = 'https://google.com'

qr = pyqrcode.create(link)
qr.png('qrcodeGoogle.png', scale = 6)
print('Qrcode gerado com sucesso')