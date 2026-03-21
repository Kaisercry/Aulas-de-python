# Definição de uma lista em python
# listaNomes = ["Dionizio","Davi","Leticia","Jessica","...",10,100,1000]

# print(listaNomes[3]) # Quarto elemento da lista
# print(listaNomes[0]) # Primeiro elemento da lista
# print(listaNomes[-1]) # Último elemento da lista
# print(listaNomes[-2]) # Penúltimo elemento da lista

# listaNomes[3] = 'Pedro'

# print(listaNomes)

# # Questão 1
# listaNumeros = [10,20,30,40,50]
# soma = listaNumeros[0] + listaNumeros[-1]
# print(soma)

# # Questão 2
# listaQualquer = [10,20,30,40,50]
# print(listaQualquer[0])

# # Questão 3 
# listaDois = [10,20,30,40,50]
# print(listaDois)
# listaDois[3] = 60
# print(listaDois)

# Fatiamento de uma lista
#               0 1 2 3 4 5 6 7  8  9
# listaNumeros = [3,4,5,6,7,8,9,10,11,12]
# lista2Numeros = listaNumeros[0:4:1]
# print(lista2Numeros)

# listaNomes = ['João', 'Maria', 'Pedro','Thiago','Carla','Jessica']

# print(lista2Numeros + listaNomes)

# print(listaNomes * 3)

# print(listaNomes[2:5])

# # Questão 1
# numerosParte1 = [0,1,2,3,4,5]
# numerosParte2 = [6,7,8,9,10]
# numerosCompletos = numerosParte1 + numerosParte2
# print(numerosCompletos)

# # Questão 2
# soma = numerosParte1[3]+numerosParte1[4]+numerosParte1[5]
# print(f'A soma dos últimos três números é: {soma}')

# # Questão 3
# print(numerosParte1 * 2)
# #---------------------------------------------------------------------------

# print(f'Lista Numeros Completos {numerosCompletos}')

# for item in numerosCompletos:
#     print(item)


# # listaNomes = ['João', 'Maria', 'Pedro','Thiago','Carla','Jessica']
# listaNomes[3] = 'Caio'
# flagAchou = False

# for nome in listaNomes:
#     if 'Caio' == nome:
#         print('O Caio faz parte da lista')
#         flagAchou = True
#         break

# if flagAchou == False:
#     print('O Caio não faz parte da lista')
    




# numeros = [1,2,3,4,5,6,7,8,9,10]

# for numero in numeros:
#     print(numero)
    
# for numero in numeros:
#     if numero % 2 != 0:
#         print(numero)


# listaNomes.append('david')
# listaNomes.insert(0,'Aline')

# print(listaNomes)

# listaNomes.pop()
# listaNomes.pop(0)
# print(listaNomes)

# del(listaNomes[2:5])

# print(listaNomes)

# Questão 1
listaVazia = []
for i in range(5):
    nome = input('Digite seu nome: ')
    listaVazia.append(nome)

print(listaVazia)
    
    
for i in range(3):
    listaVazia.pop()
  
print(listaVazia)
    
        
    
    





