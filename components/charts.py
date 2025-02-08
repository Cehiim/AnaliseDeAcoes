import plotly.express as px
import plotly.graph_objs as go

def candlestick(df, stock):
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'][stock],
        high=df['High'][stock],
        low=df['Low'][stock],
        close=df['Close'][stock],
        increasing_line_color='green',
        decreasing_line_color='red'
        )])
    fig.update_layout(
        xaxis_title='Data',
        yaxis_title='Valor',
    )
    return fig

def timeline(df):
    fig = px.line(df)
    fig.update_layout(
        xaxis_title='Data',
        yaxis_title='Valor',
        xaxis_rangeslider_visible=True
    )
    return fig

def return_period(df, option):
    fig = px.bar(df)
    fig.update_layout(
        barmode='group',
        xaxis_title='Data',
        xaxis_rangeslider_visible=True
    )
    if option == 'Bruto':
        fig.update_layout(
            yaxis_title='Valor'
        )
    else:
        fig.update_layout(
            yaxis_title='Porcentagem'
        )
    return fig