import pandas as pd

def change_table(df, dias, option):
    if option == 'Bruto':
        df_change = df.diff(dias)
    else:
        df_change = df.pct_change(dias)*100
    return df_change

def info_table(df):
    df_info = pd.DataFrame({
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
    df_info['Taxa de baixa'] = cont_negativos
    df_info['Taxa de baixa'] = df_info['Taxa de baixa'] / df.dropna().shape[0]

    # Python v3.10
    df_info = df_info.map(lambda x: f'{x:.2f}')

    #Python v3.11+
    #df_info = df_info.applymap(lambda x: f'{x:.2f}')

    return df_info