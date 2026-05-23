from supabase import create_client

supabase = create_client()

# resposta = supabase.table('employee').select('*').execute()
# resposta = resposta.data
# print(resposta)

def mostrarResultado(listaResultados):
   for resultado in listaResultados:
        for key, value in resultado.items():
            print(f'{key}: {value}')
        print('-'*30)
         

# Quetões
# 1. Liste todos os funcionário mostrando apenas o firstname, lastname e emailaddress.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 2. Mostrar os 10 funcionários mais jovens da empresa, ordenando por idade.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress,idade').order('idade').limit(10).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 3. Liste apneas os funcionário que possuem vacationhours maior = 40.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress').eq('vacationhours',40).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

'''
.eq('coluna',valor) -> igual
.neq('coluna', valor) -> diferente (não igual)
.gt('coluna',valor) -> Maior que
.gte('coluna',valor) -> Maior ou igual
.lt('coluna',valor) -> Menor que
.lte('coluna',valor) -> Menor ou igual
.like('coluna','%texto%') -> link '%texto%'
.in_('coluna',[1,2,3,...valores]) -> se esses valores constam na coluna

'''

# 4. Mostre firstname, emailaddress e departmentname dos funcionários do departamento Production.

# resposta = supabase.table('employee').select('firstname,emailaddress,departmentname').eq('departmentname','Production').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 5. Liste os funcionários cujo firstname começa com a letra A.

# resposta = supabase.table('employee').select('firstname,emailaddress').like('firstname','A%').execute()



# 6. Mostre os funcionários que possuem idade entre 30 e 50 anos.

# resposta = supabase.table('employee').select('firstname','idade').gt('idade',30).lt('idade',50).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 7. Liste firstname, idade e baserate dos funcionários com salário (baserate) maior que 60.

# resposta = supabase.table('employee').select('firstname','idade','baserate').gt('baserate',60).execute()
# resposta = resposta.data
# mostrarResultado(resposta)


# 8. Mostre os funcionários cujo emailaddress contém gmail.

# resposta = supabase.table('employee').select('firstname','emailaddress').like('emailaddress','%gmail%').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 9. Liste apenas os funcionários com currentflag = true.

# resposta = supabase.table('employee').select('firstname','currentflag').eq('currentflag','true').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 10. Mostre os funcionários do gênero masculino (gender = 'M') ordenados da maior para a menor idade.

# resposta = supabase.table('employee').select('firstname','gender').eq('gender','M').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

'''
C -> CREATE - inserir dados - Insert
R -> READ - leitura de dados - SELECT
U -> UPDATE - Atualização de dados - UPDATE
D -> DELETE - Apagar algum dado - DELETE

'''

# usuario = {
#     "nome": 'Maria',
#     "email": 'maria@gmail.com',
#     "idade": 29,
#     "senha": 'senha123'
# }
# resposta = supabase.table('usuarios').create(usuario).execute()
# print(resposta.data)

# usuario = {
#     "nome": 'Maria Clara',
#     "idade": 28
# }


# resposta = supabase.table('usuarios').update(usuario).eq('id',4).execute()
# print(resposta.data)


# resposta = supabase.table('usuarios').delete().eq('id', 1).execute()
# print(resposta.data)


def mostrarProdutos():
    resposta = supabase.table('produtos').select("nome, preco, descricao").gt('preco',100).execute()
    resposta = resposta.data
    return resposta

# print(mostrarProdutos())


def cadastrarProdutos(nome,preco,quantidade,descricao):
    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "descricao": descricao
    }
    resposta = supabase.table('produtos').insert(produto).execute()
    resposta = resposta.data
    return resposta


# print(cadastrarProdutos('Teclado', 200, 10, 'Teclado magnetico logitech'))




def atualizarPreco(preco):
    atualizar = {
        'preco': preco
    }
    resposta = supabase.table('produtos').update(atualizar).eq('id', 1).execute()
    resposta = resposta.data
    return resposta


# print(atualizarPreco(450))


def deletarProduto():
    resposta = supabase.table('produtos').delete().eq('id', 4).execute()
    resposta = resposta.data
    return resposta

print(deletarProduto())