import yfinance as yf
import numpy as np
from topicos.visao_geral import Geral

stocks = ['ITUB4.SA', 'VIVT3.SA', 'ELET3.SA', 'QBTC11.SA']
df = yf.download(stocks, start='2022-01-01', end='2025-01-01')
#df = yf.download(stocks, period='1y')

stocks = ['ITUB4.SA', 'VIVT3.SA', 'ELET3.SA', 'QBTC11.SA']
df = yf.download(stocks, start='2022-01-01', end='2025-01-01')
#df = yf.download(stocks, period='1y')

df_close = df['Close'].astype(np.float16)
df_close.rename(columns={
    'ITUB4.SA': 'Itaú (ITUB4)',
    'VIVT3.SA': 'Vivo (VIVT3)',
    'ELET3.SA': 'Eletrobrás (ELET3)',
    'QBTC11.SA': 'Bitcoin (QBTC11)'
}, inplace=True)

Geral.lineplot(df_close)

Geral.boxplot(df_close)

Geral.table(df_close)