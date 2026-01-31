import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Painel da B3", layout="wide")

st.header("**PAINEL DE PREÇO DE DIVIDENDOS DA B3**")

ticker = st.text_input("Digite o ticker da ação", "BBAS3")
empresa = yf.Ticker(f"{ticker}.SA")

tickerDF = empresa.history(start="2014-1-1", end="2025-12-31")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(f"**Empresa:** {empresa.info['longName']}")
with col2:
    st.write(f"**Setor:** {empresa.info['industry']}")
with col3:
    st.write(f"**Preço Atual:** R$ {empresa.info['currentPrice']:.2f}")

st.line_chart(tickerDF['Close'])
st.bar_chart(tickerDF['Dividends'])


