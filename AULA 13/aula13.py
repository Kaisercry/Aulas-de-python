import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)


def inserirUsuario():
    nome = input('Digite o nome do usuário: ')
    cpf = input('Digite o CPF do usuário: ')
    telefone = input('Digite o telefone do usuário: ')
    endereco = input('Digite o endereço do usuário: ')

    novoUsuario = {
        'nome': nome,
        'cpf': cpf,
        'telefone': telefone,
        'endereco': endereco
    }
    resposta = supabase.table('biblioteca_usuario').insert(novoUsuario).execute()

    print(resposta.data)

#inserirUsuario()



def inserirPerfil():
    foto = input('Digite o caminho da foto do perfil: ')
    bio = input('Digite a bio do perfil: ')
    preferencias = input('Digite as preferências do perfil: ')
    id_usuario = input('Digite o ID do usuário associado ao perfil: ')

    novoPerfil = {
        'foto': foto,
        'bio': bio,
        'preferencias': preferencias,
        'id_usuario': id_usuario
    }
    resposta = supabase.table('biblioteca_perfil').insert(novoPerfil).execute()

    print(resposta.data)

#inserirPerfil()

def inserirDadosTabela(tabela,dados):
    try:
        resposta = supabase.table(tabela).insert(dados).execute()
        print('Dados inseridos com sucesso')
    except Exception as erro:
        print(f"Erro ao inserir dados na tabela {erro}")


def atualizarDados(tabela,id,dados):
    try:
        resposta = supabase.table(tabela).update(dados).eq('id',id).execute()
        print('Dados atualizados com sucesso')
    except Exception as erro:
        print(f'Erro ao atualizar os dados: {erro}')


def deletarDados(tabela,id):
    try:
        resposta = supabase.table(tabela).delete().eq('id',id).execute()
        print('Dados deletados com sucesso')
        print(resposta)
    except Exception as erro:
        print(f'Erro ao deletar os dados: {erro}')


def coletarDadosInserir():
    opcao = input('Selecione uma opção:\n1 - Inserir Usuario\n2- Inserir Perfi\n3 - inserir Autor\n4 - Inserir Livro\n5 - Inserir Emprestimo\n')
    if opcao == '1':
        tabela = 'biblioteca_usuario'
        nome = input('Digite o nome do usuário: ')
        cpf = input('Digite o CPF do usuário: ')
        telefone = input('Digite o telefone do usuário: ')
        endereco = input('Digite o endereço do usuário: ')

        novoUsuario = {
            'nome': nome,
            'cpf': cpf,
            'telefone': telefone,
            'endereco': endereco
        }
        inserirDadosTabela(tabela,novoUsuario)
    if opcao == '2':
        tabela = 'biblioteca_perfil'
        foto = input('Digite o caminho da foto do perfil: ')
        bio = input('Digite a bio do perfil: ')
        preferencias = input('Digite as preferências do perfil: ')
        id_usuario = input('Digite o ID do usuário associado ao perfil: ')

        novoPerfil = {
            'foto': foto,
            'bio': bio,
            'preferencias': preferencias,
            'id_usuario': id_usuario
        }
        inserirDadosTabela(tabela,novoPerfil)
    if opcao == '3':
        tabela = 'biblioteca_autor'
        nome = input('Digite o nome do autor: ')
        nacionalidade = input('Digite a nacionalidade do autor: ')
        genero = input('Digite o gênero do autor: ')
        
        novoAutor = {
            'nome': nome,
            'nacionalidade': nacionalidade,
            'genero': genero
        }
        inserirDadosTabela(tabela,novoAutor)
    if opcao == '4':
        tabela = 'biblioteca_livro'
        titulo = input('Digite o título do livro: ')
        quantidade = input('Digite a quantidade de exemplares do livro: ')
        genero = input('Digite o gênero do livro: ')
        ano = input('Digite o ano de publicação do livro: ')
        id_autor = input('Digite o ID do autor do livro: ')
        novoLivro = {
            'titulo': titulo,
            'quantidade': quantidade,
            'genero': genero,
            'ano': ano,
            'id_autor': id_autor
        }
        inserirDadosTabela(tabela,novoLivro)
    if opcao == '5':
        tabela = 'biblioteca_emprestimos'
        id_usuario = input('Digite o ID do usuário que está realizando o empréstimo: ')
        id_livro = input('Digite o ID do livro que está sendo emprestado: ')
        data_emprestimo = input('Digite a data do empréstimo (formato YYYY-MM-DD): ')
        

        novoEmprestimo = {
            'id_usuario': id_usuario,
            'id_livro': id_livro,
            'data_emprestimo': data_emprestimo
        }
        inserirDadosTabela(tabela,novoEmprestimo)


def coletarDadosAtuais():
    print('Qual tabela você quer atualizar?')
    tabelas = {
        "1":"biblioteca_usuarios",
        "2":"biblioteca_perfil",
        "3":"biblioteca_autor",
        "4":"biblioteca_livro",
        "5":"biblioteca_emprestimo"
    }
    camposTabela = {
        "biblioteca_usuarios":["nome","cpf","endereco","ativo"],
        "biblioteca_perfil":["foto",'bio','preferencias'],
        "biblioteca_autor":["nome","genero","nacionalidade"],
        "biblioteca_livro":["titulo","quantidade","genero","ano"],
        "emprestimo":["data_devolucao"]
    }

    for chave, valor in tabelas.items():
        print(f'{chave} - {valor}')

    opcao = input('Digite a opcao desejada: ')
    tabelaSelecionada = tabelas[opcao]
    resposta = supabase.table(tabelaSelecionada).select('*').execute()

    print('Selecione o ID que você quer atualizar')

    for resposta in resposta.data:
        print("################################")
        for chave, valor in resposta.items():
            print(f'{chave} - {valor}')
    id = input('Digite o ID que você quer atualizar: ')

    print(tabelaSelecionada)

atualizarDados()

coletarDadosInserir()