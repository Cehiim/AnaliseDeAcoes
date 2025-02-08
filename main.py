import yfinance as yf
from components.charts import candlestick, timeline, return_period
from components.table import change_table, info_table, ma_table, corr_table
import streamlit as st

# Configuração da página
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    )

# Barra lateral
with st.sidebar:
    stock_type = st.selectbox(
        "Escolha um mercado",
        ("Nacional", "Internacional")
        )
    periods = {
        'Bissemanal': '14d',
        'Mensal': '1mo',
        'Trimestral': '3mo',
        'Bimestral': '6mo', 
        'Anual': '1y',
        'Bianual': '2y'
        }
    period_input = st.selectbox('Escolha um período', periods)

    if stock := st.text_input("Digite a sigla da ação"):
        if stock_type == "Nacional":
            stock = stock + ".SA"

        with st.spinner("Carregando dados..."):
            df = yf.download(stock, period=periods[period_input])
            df_close = df['Close']

# Abas
tab1, tab2, tab3 = st.tabs(["Gráfico de velas", "Linha do tempo", "Período de retorno"])
try:
    if df.empty:
        st.error("Dados não encontrados", icon="🚨")

    else:
        max_days = df_close.shape[0]

        # Gráfico de velas
        with tab1:
            candlestick = candlestick(df, stock)
            st.plotly_chart(candlestick)

        # Linha do tempo
        with tab2:
            window = st.slider(
                'Janela de tempo (dias)',
                min_value=2,
                max_value=max_days//2,
                value=max_days//4
                )
            df_ma = ma_table(df_close, window, stock)
            timeline = timeline(df_ma)
            st.plotly_chart(timeline)
            st.write("### Correlação com o valor real")
            df_corr = corr_table(df_ma)
            st.table(df_corr)

        # Período de retorno
        with tab3:
            days = st.slider(
                'Intervalo de retorno (dias)',
                min_value=1,
                max_value=max_days//2,
                value=max_days//4
                )
            option = st.selectbox(
                'Opção de retorno',
                ('Percentual', 'Bruto')
            )
            df_change = change_table(df_close, days, option)
            return_period = return_period(df_change, option)
            st.plotly_chart(return_period)
            df_info = info_table(df_change)
            st.table(df_info)

except NameError:
    st.warning("É necessário selecionar uma ação", icon="⚠️")
