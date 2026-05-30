import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')

supabase = create_client(supabase_url,supabase_key)

resposta = (supabase.table('pedidos').select('id, valor, forma_pagamento,usuarios(nome)').eq('id_usario',1).execute())

print(resposta.data)


resposta = (supabase.table('itens_pedidos').select('nome, pedidos,(id,valor,usuarios(nome))').execute())

print(resposta.data)

resposta = supabase.table('matriculas').select('alunos(nome), curso(nome)').eq('id_aluno',1).execute()

for resp in resposta.data:
    print(f'{resp['alunos']['nome']} : {resp['curso']['nome']}')
