import streamlit as st
import pandas as pd
st.subheader('1.读入数据')
df = pd.read_csv('NSE-TATAGLOBAL11.csv')
st.dataframe(df)
