# Análise de Ações

## Bibliotecas usadas
* `yfinance`: Extração dos dados das ações
* `streamlit`: Desenvolvimento da interface interativa
* `plotly`: Criação de gráficos interativos
* `pandas`: Manipulação dos dados

## Como usar
1. Instalar as dependências no arquivo `requirements.txt`.
2. Executar com `streamlit run main.py`.

## Descrição
### Candlesticks
![image](https://github.com/user-attachments/assets/3558a1e3-8eab-4480-9a8b-1562c7f83f4d)

* Apresenta uma visão geral contendo o valor de abertura, fechamento, máximo e mínimo de cada dia.
* A cor verde indica um valor de fechamento maior que o de abertura, enquanto o vermelho indica o contrário.

### Gráfico de linhas
![image](https://github.com/user-attachments/assets/1c3da1ef-b2ae-43bf-8efc-d5b86cad74b5)

* Apresenta uma série temporal do valor de fechamento de cada dia e as médias móveis.
* Há um controle deslizante para definir a janela de tempo das médias móveis. O padrão foi definido como um 1/4 aproximado do número de amostras totais.
* A linha branca indica o valor real, a verde indica a média móvel simples (SMA) e a vermelha indica a média móvel exponencial (EMA).

### Gráfico de barras
![image](https://github.com/user-attachments/assets/2f74b709-135d-4f36-9ddf-f94cfb395552)

* Apresenta a diferença do valor de fechamento em um intervalo de tempo.
* Há um controle deslizante para definir o intervalo de retorno em que será comparado. O padrão foi definido como um 1/4 aproximado do número de amostras totais.
* Há uma caixa de seleção para optar em visualizar os valores em porcentagem ou em forma bruta.
* Há uma tabela reunindo medidas estatísticas referentes ao gráfico.

## Insights
* Foi utilizado o histórico trimestral (07/11/2024 - 07/02/2025) dos valores das ações do Itaú e Eletrobrás para a análise de dados com o dashboard desenvolvido.
* Foi usado o valor padrão de 15 dias nos controles deslizantes.

### Itaú
![image](https://github.com/user-attachments/assets/b082c441-38c3-46ef-b56e-27caa5a59ec3)

* Próximo ao dia 12/01 é possível observar uma maior estabilidade na SMA, o que indica uma redução na queda de preços e do risco.
* O cruzamento da linha real com a SMA indica uma tendência de valorização.

![image](https://github.com/user-attachments/assets/8ec5da7d-5e5d-4836-af36-eee8120ef025)

* Dia 13/01 e 14/01 seriam períodos ideais para comprar e aproveitar a valorização.

### Eletrobrás
![image](https://github.com/user-attachments/assets/2a145f91-b4e6-4287-bbf7-c660b7935191)

* Próximo ao dia 12/01 é possível observar uma maior estabilidade na SMA, o que indica uma redução na queda de preços e do risco.
* O cruzamento da linha real com a SMA indica uma tendência de valorização.
* O intervalo de oportunidade é curto, é necessário acompanhar com atenção.

![image](https://github.com/user-attachments/assets/a8faefdc-0abd-42c4-88fb-f6d25dfaadfa)

* Próximo ao dia 02/02 é possível observar uma maior estabilidade na EMA, o que indica uma redução na valorização de preços.
* O cruzamento da linha real com a EMA indica uma tendência de desvalorização.

![image](https://github.com/user-attachments/assets/76248a48-d305-4c85-8cb9-59b818fbbb70)

* Dia 13/01 e 14/01 seriam períodos ideais para comprar e aproveitar a valorização.
* Dia 06/02 e 07/02 seriam períodos recomendados para vender as ações e evitar perdas.
