import streamlit as st
import pandas as pd
import numpy as np
st.subheader('读入数据')
df = pd.read_csv('NSE-TATAGLOBAL11.csv')
st.dataframe(df)

st.subheader('选择时间序列')
options = np.array(df['Date']).tolist()

(start_time, end_time) = st.select_slider("请选择时间序列长度：",
     options = options,
     value= ('2016-05-04','2014-06-27',),
 )
st.write("时间序列开始时间:",end_time)
st.write("时间序列结束时间:",start_time)


df['Date'] = pd.to_datetime(df.Date, format = '%Y-%m-%d')
df.index = df['Date']

df = df[start_time:end_time]
st.dataframe(df)

number = st.number_input("请输入训练集所占比例：",min_value=0.5,max_value=0.9,value=0.8,step=0.1)
split = int(number * len(df))
st.write("选择的数据集大小：",len(df))
st.write("训练集大小：",split)
st.write("预测集大小：",len(df)-split)
