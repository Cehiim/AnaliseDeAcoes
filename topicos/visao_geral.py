import streamlit as st
import plotly.express as px
import pandas as pd

class Geral:

    @staticmethod
    def lineplot(df):
        fig = px.line(df)
        fig.update_layout(
            xaxis_title='Datas',
            yaxis_title='Valores (R$)',
            legend={
                'title': 'Ações',
            }
        )
        st.plotly_chart(fig)

    @staticmethod
    def table_change(df):
        df_resumo = pd.DataFrame({
            'Média': df.mean(),
            'Variância': df.var(),
            'Mínimo': df.min(),
            'Máximo': df.max(),
            'Q1': df.quantile(0.25),
            'Mediana': df.quantile(0.5),
            'Q3': df.quantile(0.75),
            'IQR': df.quantile(0.75) - df.quantile(0.25),
        })
        cont_negativos = []
        for column in df.columns:
            cont_negativos.append(df.loc[df[column] < 0].shape[0])
        df_resumo['Taxa de perda'] = cont_negativos
        df_resumo['Taxa de perda'] = df_resumo['Taxa de perda'] / df.shape[0]
        df_resumo = df_resumo.map(lambda x: f'{x:.2f}')
        st.table(df_resumo)

    def change(df, period_input):
        if(period_input == '7d'):
            dias_max = 3
        elif(period_input == '1mo' or period_input == '3mo'):
            dias_max = 7
        elif(period_input == '6mo'):
            dias_max = 30
        else:
            dias_max = 90
        dias = st.slider('Intervalo de retorno (dias)', min_value=1, max_value=dias_max, value=3)
        option = st.selectbox(
            'Opção de retorno:',
            ('Percentual', 'Bruto')
        )
        if option == 'Bruto':
            df_change = df.diff(dias)
            fig = px.line(df_change)
            fig.update_layout(
                xaxis_title='Datas',
                yaxis_title='Valores (R$)',
                legend={
                    'title': 'Ações',
                }
            )
        else:
            df_change = df.pct_change(dias)*100
            fig = px.line(df_change)
            fig.update_layout(
                xaxis_title='Datas',
                yaxis_title='Porcentagem',
                legend={
                    'title': 'Ações',
                }
            )
        st.plotly_chart(fig)
        Geral.table_change(df_change)