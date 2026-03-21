print('Olá mundo!')

# Aqui falaremos sobre variáveis
numero = 10
Numero = 20
NUMERO = 30

print(numero, Numero, NUMERO)

# Hardcode
x = 10
y = 2

# Soma
soma = x + y
print('soma = ',soma)

#Subtração
subtracao = x - y
print(subtracao)

# Multiplicação
multiplicacao = x * y
print(multiplicacao)

# Divisão
divisao = x/y
print(divisao)

# Resto da divisão
resto = x % y
print('O resto é ',resto)

# Potência
potencia = x ** y
print(x,' elevado a ',y,' = ',potencia)

# Divisao por inteiro
divisaoInteiro = x//y
print(divisaoInteiro)

# Operadores de atribuição
# =
a = 2
# +=
a += 3
a -= 1
a *= 2
a /= 4
a **= 2 # a = 4
b = a/3 # b = 1.33333....
a //= 3 # a = 1

c = b - a  # 1.333... - 1 = 0.333....
print(c)

# Operadores Relacionais

a = 10
b = 5
print(a > b) # True
print(a < b) # False
print(a >= b) # True
print(a <= b) # False
print(a == b) # False
print(a != b) # True

sol = False
dinheiro = False
print('Praia (and): ', sol and dinheiro)
print('Praia (or): ', sol or dinheiro)

a = 10 > 2 # True

print(not a)

# potencias e raizes
# Multiplicações e Divisões
# Soma e subtração

a = (10 + 2) * 3

print(a)
n1 = 10
n2 = 8
n3 = 6

media = (n1 + n2 + n3) / 3

print(media)

# Entrada de dados

#nome = input('Digite o seu nome: ')
#print('Olá ',nome)

x = input('Digite o primeiro número: ')
y = input('Digite o segundo número: ')

# casting
x = int(x)
y = int(y)


print('O resultado da soma é ' , (x + y))

# Escreva um programa em python que receba do usuário 2 números e mostre o resultado da soma, subtração, divisão e multiplicação desses números.


