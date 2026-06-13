# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install supabase
# pip install python-dotenv
# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env

import os
import string
from dotenv import load_dotenv
from supabase import create_client #
from fastapi import FastAPI
import requests

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) #
# CRUD

app = FastAPI()



# produtos = requests.get('https://fakestoreapi.com/products/1').json()


# print(produtos)



# CEP = input('Digite o seu CEP: ')

# endereco = requests.get(f'https://viacep.com.br/ws/{CEP}/json/').json()

# print(f'Cidade: {endereco['localidade']}\nSua rua: {endereco['logradouro']}\nEstado: {endereco['estado']}')




#criação das primeiras rotas da API

# @app.get('/livros')
# def get_livros():
#     resposta = supabase.table('biblioteca_livro').select('*').execute()
#     livro = resposta.data
#     return livro


# @app.get('/livros/{id}')
# def get_livros_id(id: int):
#     resposta = supabase.table('biblioteca_livro').select('*').eq('id',id).execute()
#     livro = resposta.data

#     if len(livro) == 0:
#         return {'mensagem: Livro não encontrado'}
    
#     return livro


#1. questão

@app.get('/usuario')
def get_usuario():
    resposta = supabase.table('biblioteca_usuario').select('*').execute()
    livro = resposta.data
    return livro



@app.get('/usuario/{cpf}')
def get_usuario_cpf(cpf = int):
    resposta = supabase.table('biblioteca_usuario').select('*').eq('cpf',cpf).execute()
    livro = resposta.data
    return livro


@app.get('/livro/{id_autor}')
def get_autor_livro(id_autor = int):
    resposta = supabase.table('biblioteca_livro').select('*').eq('id_autor',id_autor).execute()
    livro = resposta.data
    return livro