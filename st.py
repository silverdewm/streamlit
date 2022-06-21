import streamlit as st
import pandas as pd
import numpy as np
from LinearRegression import  LinearRegression
from MovingAverage import MovingAverage
from KNearestNeighbours import KNearestNeighbours
from AutoARIMA import AutoARIMA
from LongShortTM import LongShortTM

df = pd.read_csv('NSE-TATAGLOBAL11.csv')
number = st.number_input("请输入训练集所占比例：",min_value=0.5,max_value=0.9,value=0.8,step=0.1)
split = int(number * len(df))
st.write("选择的数据集大小：",len(df))
st.write("训练集大小：",split)
st.write("预测集大小：",len(df)-split)
st.subheader('选择预测目标')
type = st.selectbox('请选择预测目标：',('Close','Turnover (Lacs)'))
st.line_chart(df[type])
st.subheader('选择机器学习算法')
genre = st.selectbox("请选择时间序列预测算法",
     ('移动平均算法', '线性回归算法', '最近邻算法', 'AutoARIMA算法', 'LSTM算法'))
if genre == '移动平均算法':
    MovingAverage(df, type, split)
elif genre == '线性回归算法':
     LinearRegression(df, type, split)
elif genre == '最近邻算法':
     KNearestNeighbours(df, type, split)
elif genre == 'AutoARIMA算法':
    AutoARIMA(df, type, split)
elif genre == 'LSTM算法':
    LongShortTM(df, type, split)
