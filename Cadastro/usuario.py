import streamlit as st
cadastroUsuarios = [
    {'nome': 'João', 
     'idade': 30, 
     'cidade': 'São Paulo', 
     'telefone': 85858585
    },
    {'nome': 'Maria',
     'idade': 25, 
     'cidade': 'Rio de Janeiro', 
     'telefone': 96969696
    }
]
st.title('Cadastro de Usuário')

nome = st.text_input('Digite o seu nome')
idade = st.text_input('Digite a sua idade')
cidade = st.text_input('Digite a sua cidade')
telefone = st.text_input('Digite o seu telefone')
if st.button('Cadastrar'):
    st.write(f'Usuário {nome} cadastrado com sucesso!')
    st.write(f'Telefone: {telefone}')