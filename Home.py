import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
)

st.title("Trading Guide")
st.header("Welcome to the Trading Application! We are here to help you trade smarter.")
st.image("pic.jpg", caption="Trade Smart, Trade Easy")

company_data = pd.DataFrame(
    {
        "Company": [
            "Apple",
            "Tesla",
            "Microsoft",
            "Amazon",
            "Alphabet",
            "Meta",
            "NVIDIA",
            "JPMorgan Chase",
            "Visa",
            "UnitedHealth",
        ],
        "Code": ["AAPL", "TSLA", "MSFT", "AMZN", "GOOGL", "META", "NVDA", "JPM", "V", "UNH"],
    }
)

st.subheader("Available Company Codes")
with st.container(height=260):
    st.dataframe(company_data, width="stretch")

st.markdown("### Our Main Features")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Stock Analysis")
    st.write(
        "This page lets you analyze a company using live market data, historical prices, and key financial metrics. "
        "You can compare price movement, view charts, and use technical indicators such as SMA, EMA, RSI, and MACD to understand trends."
    )
    if st.button("Go to Stock Analysis", use_container_width=True):
        st.switch_page("pages/Stock_Analysis.py")

with col2:
    st.markdown("### 🤖 Stock Prediction")
    st.write(
        "This page helps forecast future stock prices using historical patterns and predictive modeling. "
        "It gives you a practical view of possible upcoming price movements for selected companies."
    )
    if st.button("Go to Stock Prediction", use_container_width=True):
        st.switch_page("pages/Stock_Prediction.py")
