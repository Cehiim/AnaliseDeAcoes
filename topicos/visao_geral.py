import streamlit as st
import plotly.express as px

class Geral:

    @staticmethod
    def lineplot(df):
        st.write('''
        ### Linha do tempo
        ''')

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
    def boxplot(df):
        st.write('''
        ### Distribuição
        ''')

        fig = px.box(df)

        fig.update_layout(
            xaxis_title='Ações',
            yaxis_title='Valores (R$)'
        )

        st.plotly_chart(fig)

    @staticmethod
    def table(df):
        st.write('''
        ### Tabela descritiva
        ''')

        df_resumo = df.describe().transpose()
        df_resumo = df_resumo.drop(columns=['count','mean'])
        new_order = ['min', 'max', 'std', '25%',	'50%', '75%']
        df_resumo = df_resumo[new_order]

        df_resumo.rename(columns={
            #'count': 'Nº de amostras',
            #'mean': 'Média',
            'std': 'Desvio padrão',
            'min': 'Mín.',
            'max': 'Máx.',
            '25%': 'Q1 (25%)',
            '50%': 'Q2/Mediana (50%)',
            '75%': 'Q3 (75%)'
        }, inplace=True)

        df_resumo['IQR'] = df_resumo['Q3 (75%)'] - df_resumo['Q1 (25%)']

        df_resumo = df_resumo.map(lambda x: f'{x:.2f}')

        st.table(df_resumo)