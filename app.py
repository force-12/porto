import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Portfolio M. Irfan Rahman", layout="wide")

# baca file html
with open("portfolio.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# tampilkan di streamlit
components.html(html_code, height=900, scrolling=True)
