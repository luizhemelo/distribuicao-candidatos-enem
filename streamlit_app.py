import streamlit as st
import streamlit.components.v1 as components

p = open("vis.html")
components.html(p.read())
