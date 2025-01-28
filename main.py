import yfinance as yf
import streamlit as st
import plotly.express as px

stocks = ['ITUB4.SA', 'VIVT3.SA', 'ELET3.SA', 'QBTC11.SA']
df = yf.download(stocks, start='2022-01-01', end='2025-01-01')
#df = yf.download(stocks, period='1y')

df_close = df['Close']
df_close = df_close.map(lambda x: f"{x:.2f}")
df_close.rename(columns={
    'ITUB4.SA': 'Itaú',
    'VIVT3.SA': 'Vivo',
    'ELET3.SA': 'Eletrobrás',
    'QBTC11.SA': 'Bitcoin'
}, inplace=True)

st.write('''
# Visão Geral
''')

fig = px.line(df_close)
fig.update_layout(
    xaxis_title='Datas',
    yaxis_title='Valores (R$)',
    legend=dict(
        title='Ações'),
    yaxis=dict(
        #range=[0, 60],
        #dtick=2,
        type='linear',
    )
)
st.plotly_chart(fig)