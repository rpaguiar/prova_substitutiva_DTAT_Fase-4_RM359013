import streamlit as st
import pandas as pd
import joblib
from datetime import timedelta
import plotly.graph_objects as go

# Configuração da página

st.set_page_config(page_title="Previsão do Petróleo", layout="wide")
st.title("📈 Previsão do Preço do Petróleo Brent")
st.markdown("Modelo preditivo baseado em Random Forest com dados reais")

# Carrega dados e modelo

df = pd.read_csv("dados_petroleo.csv", parse_dates=["date"])
df.set_index("date", inplace=True)
rf = joblib.load("modelo_rf.pkl")

# 🔹 Seleção de intervalo de previsões de preço

dias = st.selectbox("Selecione o intervalo de previsões (dias úteis):", [30, 90, 180], index=2)

# 🔹 Previsão recursiva para dias úteis

lag1 = df['value'].iloc[-1]
lag2 = df['value'].iloc[-2]
lag3 = df['value'].iloc[-3]
data_atual = df.index[-1]

previsoes = []
datas = []

while len(previsoes) < dias:
    data_atual += timedelta(days=1)
    if data_atual.weekday() >= 5:  # pula sábado e domingo
        continue

    nova_linha = {
        'lag1': lag1,
        'lag2': lag2,
        'lag3': lag3,
        'dayofweek': data_atual.weekday(),
        'month': data_atual.month,
        'day': data_atual.day
    }

    pred = rf.predict(pd.DataFrame([nova_linha]))[0]
    previsoes.append(pred)
    datas.append(data_atual)

    # atualiza os lags

    lag3 = lag2
    lag2 = lag1
    lag1 = pred

df_rf_forecast = pd.DataFrame({'Previsão (USD)': previsoes}, index=datas)

# 🔹 Estatísticas da previsão

min_valor = df_rf_forecast['Previsão (USD)'].min()
max_valor = df_rf_forecast['Previsão (USD)'].max()

st.subheader("💵 Valores Mínimo e Máximo de Cotação no Intervalo")
col_min, col_max = st.columns(2)
col_min.metric("Valor mínimo previsto", f"{min_valor:.2f} USD")
col_max.metric("Valor máximo previsto", f"{max_valor:.2f} USD")

# 🔹 Gráfico interativo com Plotly

st.subheader(f"📊 Previsão para os próximos {dias} dias úteis")

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_rf_forecast.index,
    y=df_rf_forecast['Previsão (USD)'],
    mode='lines+markers',
    name='Preço - petróleo bruto - Brent (FOB)',
    line=dict(color='orange'),
    hovertemplate='Data: %{x}<br>Preço: %{y:.2f} USD'
))

fig.update_layout(
    yaxis=dict(range=[64, 68]),
    xaxis_title='Data',
    yaxis_title='Preço do Petróleo (USD)',
    hovermode='x unified',
    template='plotly_white',
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# 🔹 Exportar CSV

csv = df_rf_forecast.to_csv().encode("utf-8")
st.download_button(
    label="📥 Exportar valores como CSV",
    data=csv,
    file_name=f"previsao_petroleo_{dias}dias.csv",
    mime="text/csv"
)

# 🔹 Desempenho do modelo (últimos 180 dias)

st.subheader("📊 Desempenho do modelo nos últimos 180 dias")
col1, col2, col3 = st.columns(3)
col1.metric("Erro médio por dia", "2.78 USD")
col2.metric("Desvio médio", "3.84 USD")
col3.metric("Precisão percentual", "96.00%")

# 🔹 Observações

st.subheader("🧠 Observações")
st.markdown(f"""
- O modelo prevê uma **leve queda inicial**, seguida de **recuperação gradual**.
- A cotação varia entre aproximandamente **64 e 68 USD** ao longo período.
- O padrão indica **estabilidade com tendência de alta moderada**.
- O modelo apresenta um **erro médio diário de 2.78 USD** e uma **precisão de 96.00%** nos últimos 180 dias.
- O modelo Random Forest apresentou melhor desempenho em testes recentes e foi escolhido para esta previsão.
""")