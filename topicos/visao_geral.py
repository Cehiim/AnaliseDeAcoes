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
        df_resumo = df_resumo.map(lambda x: f'{x:.2f}')
        st.table(df_resumo)

    def change(df, period_input):
        if(period_input == '7d'):
            dias_max = 3
        elif(period_input == '1mo'):
            dias_max = 7
        elif(period_input == '3mo'):
            dias_max = 15
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
            fig = px.bar(df_change)
            fig.update_layout(
                barmode='group',
                xaxis_title='Datas',
                yaxis_title='Valores (R$)',
                legend={
                    'title': 'Ações',
                }
            )
        else:
            df_change = df.pct_change(dias)*100
            fig = px.bar(df_change)
            fig.update_layout(
                barmode='group',
                xaxis_title='Datas',
                yaxis_title='Porcentagem',
                legend={
                    'title': 'Ações',
                }
            )
        st.plotly_chart(fig)
        Geral.table_change(df_change)