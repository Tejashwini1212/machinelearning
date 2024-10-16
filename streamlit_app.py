import streamlit as st
import pandas as pd

st.title('🦾Machine Learning App')

st.info('This application constructs a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Tejashwini1212/dataset/refs/heads/main/iris.csv')
  df


