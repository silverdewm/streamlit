import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv('NSE-TATAGLOBAL11.csv')
st.subheader('选择时间序列')
options = np.array(df['Date']).tolist()

(start_time, end_time) = st.select_slider("请选择时间序列长度：",
     options = options,
     value= ('2016-05-04','2014-06-27',),
 )
st.write("时间序列开始时间:",end_time)
st.write("时间序列结束时间:",start_time)

#setting index as date
df['Date'] = pd.to_datetime(df.Date, format = '%Y-%m-%d')
df.index = df['Date']

df = df[start_time:end_time]
st.dataframe(df)
