import yfinance as yf
from topicos.visao_geral import Geral
import streamlit as st

stocks = ['ITUB4.SA', 'VIVT3.SA', 'ELET3.SA', 'QBTC11.SA']
options = st.multiselect('Selecione uma ou mais ações', stocks)

try:
    df = yf.download(options, start='2022-01-01', end='2025-01-01')

    df_close = df['Close']
    df_close.rename(columns={
        'ITUB4.SA': 'Itaú (ITUB4)',
        'VIVT3.SA': 'Vivo (VIVT3)',
        'ELET3.SA': 'Eletrobrás (ELET3)',
        'QBTC11.SA': 'Bitcoin (QBTC11)',
        }, inplace=True)

    st.write('''
    ### Linha do tempo
    ''')
    Geral.lineplot(df_close)

    st.write('''
    ### Retorno
    ''')
    Geral.change(df_close, '1y')

except ValueError:
    st.write("Selecione pelo menos uma ação")