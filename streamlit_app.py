import streamlit as st
import streamlit.components.v1 as components
st.set_page_config(layout="wide")

p = open("vis.html")
components.html(p.read())
