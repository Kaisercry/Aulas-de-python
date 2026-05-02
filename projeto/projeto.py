import streamlit as st
import pyqrcode as qr
import pyttsx3

robo = pyttsx3.init()
st.title('Gerador de QRcode')

# 1. entrada de dados
nome = st.text_input('Qual o seu nome?')
telefone = st.text_input('Qual o seu telefone?')
mensagem = st.text_area('Digite a mensagem que deseja enviar')

if st.button('Enviar'):
    link = f'https://api.whatsapp.com/send?phone={telefone}&text={mensagem}&type=phone_number&app_absent=0'

    qrcode = qr.create(link)
    qrcode.png('qrcode_aula.png', scale=3)
    st.write(f'QRcode gerado com sucesso!')
    st.image('qrcode_aula.png')
    st.write(f'Link gerado com sucesso!')
    st.write(link)
    robo.say(f'QRcode e link foram gerados com sucesso!')
    robo.runAndWait()