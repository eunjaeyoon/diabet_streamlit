import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda_app() :
    st.subheader('데이터 분석')

    df = pd.read_csv('data/diabetes.csv')

    st.dataframe( df )
    
    st.subheader('Nan 데이터 확인')

    st.dataframe( df.isna().sum())

    st.subheader('각 컬럼별 히스토그램 확인')
