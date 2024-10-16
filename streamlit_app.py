import streamlit as st
import pandas as pd

st.title('🦾Machine Learning App')

st.info('This application constructs a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Tejashwini1212/dataset/refs/heads/main/iris.csv')
  df

  st.write('**X**')
  X = df.drop('Sepal.Length', axis=1)
  X

  
  st.write('**y**')
  y = df['Sepal.Length']
  y
  
  with st.expander('Data Visualization'):
    st.write("Scatter plot: Sepal.Width vs Petal.Width with color representing Sepal.Length")

# Create scatter plot using Altair
scatter_plot = alt.Chart(df).mark_circle(size=60).encode(
    x='Sepal.Width',
    y='Petal.Width',
    color='Sepal.Length',
    tooltip=['Sepal.Length', 'Sepal.Width', 'Petal.Length', 'Petal.Width', 'Species']  # Tooltip for more info
).interactive()  # Enable zoom and pan

# Display the Altair chart
st.altair_chart(scatter_plot, use_container_width=True)
