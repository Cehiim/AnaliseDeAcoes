import streamlit as st
import plotly.express as px
from components.table import info_table

def timeline(df):
    fig = px.line(df)
    fig.update_layout(
        xaxis_title='Datas',
        yaxis_title='Valores (R$)',
        legend={
            'title': 'Ações',
        }
    )
    st.plotly_chart(fig)

def gain_period(df, option):
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
    info_table(df_change)