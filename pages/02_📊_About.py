import streamlit as st
import pandas as pd
import datetime
from modules.formater import Title

# Title page and footer
title = "📊 About"
Title().page_config(title)

st.markdown("## 📊 About")

st.markdown("""
Open-sourcing job requirements for aspiring data analysts is necessary for data nerds to focus more efficiently on what skills they need to learn for their future job. This dashboard is only the beginning of that journey. \n 
""")