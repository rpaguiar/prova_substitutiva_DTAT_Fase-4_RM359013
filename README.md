# Prova Substitutiva – Fase 4 – Pós-Tech FIAP

Criar um modelo preditivo para garantir qual será a previsão do preço do petróleo em dólar e instanciar esse modelo preditivo em uma aplicação para auxiliar na tomada de decisão.

---

## Objetivo – Previsão do Preço do Petróleo Brent

Este projeto utiliza aprendizado de máquina para prever o preço do petróleo Brent com base em dados históricos. O modelo principal é o **Random Forest**, treinado com variáveis de data e defasagens (lags), e integrado a um painel interativo em **Streamlit**.

---

## Modelos Avaliados

Durante o desenvolvimento, foram testados dois modelos de previsão:

| Modelo         | MAE   | RMSE  | MAPE   | Precisão |
|----------------|-------|-------|--------|----------|
| SARIMA         | 5.24  | 6.16  | 7.51%  | 92.49%   |
| Random Forest  | 2.78  | 3.84  | 4.00%  | 95.68%   |

> O modelo **Random Forest** foi escolhido para o painel por apresentar menor erro médio e maior precisão nas previsões de curto e médio prazo.

---

## Link da Aplicação

Deploy disponível em:  
🔗 [https://prova-substitutiva-dtat-fase-4-rm359013.streamlit.app](https://prova-substitutiva-dtat-fase-4-rm359013.streamlit.app)

---

## Funcionalidades do Painel

- Previsão para 30, 90 ou 180 dias úteis
- Gráfico interativo com Plotly
- Exportação das previsões como CSV
- Métricas de desempenho dos modelos
- Intervalo previsto com valores mínimo e máximo
- Observações dinâmicas conforme o período selecionado

---

## Estrutura do Projeto

- `app.py` → Código do dashboard Streamlit  
- `modelo_rf.pkl` → Modelo Random Forest treinado e salvo  
- `dados_petroleo.csv` → Base com dados do preço do petróleo  
- `requirements.txt` → Lista de dependências do projeto  
- `README.md` → Documentação geral  

---

## Tecnologias Utilizadas

- Python 3.10+
- Streamlit
- scikit-learn
- statsmodels
- pandas
- plotly
- joblib
