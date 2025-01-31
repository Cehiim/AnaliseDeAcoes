import yfinance as yf
from topicos.visao_geral import Geral
import streamlit as st

stock = st.text_input("Digita uma ação nacional") + '.SA'

periods = {
    'Semanal': '7d',
    'Mensal': '1mo',
    'Trimestral': '3mo',
    'Bimestral': '6mo', 
    'Anual': '1y'
    }
period_input = st.selectbox('Escolha um período', periods)

try:
    df = yf.download(stock, period=periods[period_input])

    df_close = df['Close']

    st.write('''
    ## Linha do tempo
    ''')
    Geral.lineplot(df_close)

    st.write('''
    ## Retorno
    ''')
    Geral.change(df_close, periods[period_input])

except ValueError:
    st.write("Selecione pelo menos uma ação")