import yfinance as yf
from components.charts import timeline, gain_period
import streamlit as st

# Configuração da página
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    )

stock = st.text_input("Digita uma ação nacional") + '.SA'

periods = {
    'Semanal': '7d',
    'Mensal': '1mo',
    'Trimestral': '3mo',
    'Bimestral': '6mo', 
    'Anual': '1y'
    }
period_input = st.selectbox('Escolha um período', periods)

if stock != ".SA":
    df = yf.download(stock, period=periods[period_input])
    df_close = df['Close']
    tab1, tab2 = st.tabs(["Linha do tempo", "Período de ganho"])

else:
    st.write("Selecione uma ação")

    try:
        with tab1:
            st.write('''
            ## Linha do tempo
            ''')
            timeline(df_close)

        with tab2:
            st.write('''
            ## Retorno
            ''')
            dias_max = df_close.shape[0]
            dias = st.slider('Intervalo de retorno (dias)', min_value=1, max_value=dias_max//2, value=dias_max//4)
            option = st.selectbox(
                'Opção de retorno:',
                ('Percentual', 'Bruto')
            )
            gain_period(df_close, option)

    except NameError:
        st.write