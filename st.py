import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('NSE-TATAGLOBAL11.csv')
number = st.number_input("请输入训练集所占比例：",min_value=0.5,max_value=0.9,value=0.8,step=0.1)
split = int(number * len(df))
st.write("选择的数据集大小：",len(df))
st.write("训练集大小：",split)
st.write("预测集大小：",len(df)-split)
st.subheader('选择预测目标')
type = st.selectbox('请选择预测目标：',('Close','Turnover'))
st.line_chart(df[type])
