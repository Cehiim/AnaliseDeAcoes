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
Foi utilizado o histórico dos valores das ações da Vivo, Itaú, Eletrobrás e Bitcoin para explorar a biblioteca Streamlit na criação de dashboards interativos.

## Resultados
![image](https://github.com/user-attachments/assets/8d616183-5619-4d7c-9e7c-e91cb0e2a053)

Foi criado um gráfico de linha com os dados de fechamento de preço de cada dia durante o período de 01/10/2024 até 01/01/2025.

![image](https://github.com/user-attachments/assets/6de0fb88-7a6d-4fe1-b0fa-a8abb9909207)
![image](https://github.com/user-attachments/assets/dc2b3e4b-68f4-46a5-9e0e-3e1bba1ebadb)

Foi criado um gráfico de barras que apresenta a diferença de preços durante um intervalo de tempo, também é possível alternar em mostrar as diferenças em porcentagem ou em valor bruto.

![image](https://github.com/user-attachments/assets/8edaf502-434c-4def-8c9b-f78f7a4099ee)

Foi criado uma tabela com base no gráfico de retorno para auxiliar na análise. Com os valores mínimos, valores máximos, variância, IQR (intervalo interquartílico), diferença da mediana com o 1º quartil, diferença do 3º quartil com a mediana e a taxa de baixa (qtd. de baixas ÷ qtd. de instâncias)

## Insights

### Vivo
![image](https://github.com/user-attachments/assets/62c2bc3e-7d0a-4037-a330-30d917b17905)

* É possível visualizar uma taxa maior de baixas, porém a partir da 3ª semana de dezembro os picos de prejuízo passaram a diminuir de tamanho, o que pode dar mais segurança no investimento.
* Não há muita consistência no comportamento dos retornos positivos, o que torna difícil de prever um bom resultado.
* A diferença entre quartis mostra que considerando apenas os dados normalizados, houve mais retornos abaixo do valor da mediana do que acima.

### Itaú
![image](https://github.com/user-attachments/assets/c0512794-1c19-4b23-a585-b860c134beb7)

* A partir da 3ª semana de dezembro os picos de prejuízo passaram a diminuir de tamanho, o que pode dar mais segurança no investimento.
* Não há muita consistência no comportamento dos retornos positivos, o que torna o investimento mais arriscado.

### Eletrobrás
![image](https://github.com/user-attachments/assets/f16e6523-abc3-4029-8105-57126131a5e7)

* Durante a última semana de dezembro, os retornos variaram menos e estavam próximos do normal.
* De acordo com a diferença de quartis, houve mais valores normais acima da mediana, porém deve-se ressaltar que a mediana tem um abaixo de 0.

### Bitcoin
![image](https://github.com/user-attachments/assets/9e4a0f51-0e27-4a39-a33e-5990678b714d)

* Analisando o valor da variância e do IQR, é possível afirmar que as ações do Bitcoin tem uma volatilidade anormal, o que aumenta o risco de investimento.
* Apesar de haver pouca frequência de baixas e o pico de retorno positivo ser maior que o de retorno negativo, é possível visualizar uma tendência de aumento no prejuízo em retornos negativos, ou seja, no pior caso haverá um prejuízo maior que os passados.
* Além disso, há uma tendência do valor de returnos positivos reduzirem, visto que durante a 3ª semana de novembro os picos de valorização diminuíram progressivamente.

### Opinião
* Acredito que a ação com menos risco dos quatro seria da Eletrobrás.
* Poderia ser interessante acompanhar as ações da Vivo e do Itaú, pois parece que haverá uma redução do tamanho dos picos de prejuízo.
* Por fim, acho que Bitcoin apresentará um risco de investimento maior no futuro.
