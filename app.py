import streamlit as st

pages = [
    st.Page("Home.py", title="Home", icon="🏠", default=True),
    st.Page("pages/Stock_Analysis.py", title="Stock Analysis", icon="📊"),
    st.Page("pages/Stock_Prediction.py", title="Stock Prediction", icon="🤖"),
]

navigation = st.navigation(pages)
navigation.run()
