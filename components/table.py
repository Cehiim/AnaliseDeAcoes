import pandas as pd
import streamlit as st

def info_table(df):
    df_resumo = pd.DataFrame({
        'Mínimo': df.min(),
        'Máximo': df.max(),
        'Variância': df.var(),
        'Mediana': df.quantile(0.5),
        'IQR': df.quantile(0.75) - df.quantile(0.25),
        'Q2 - Q1': df.quantile(0.5) - df.quantile(0.25),
        'Q3 - Q2': df.quantile(0.75) - df.quantile(0.5),
    })
    cont_negativos = []
    for column in df.columns:
        cont_negativos.append(df.loc[df[column] < 0].dropna().shape[0])
    df_resumo['Taxa de baixa'] = cont_negativos
    df_resumo['Taxa de baixa'] = df_resumo['Taxa de baixa'] / df.dropna().shape[0]
    df_resumo = df_resumo.applymap(lambda x: f'{x:.2f}')
    st.table(df_resumo)