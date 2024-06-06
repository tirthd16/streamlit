import streamlit as st
import pandas as pd

data = pd.read_csv('../csv/amazon_corrected.csv')
# Extract number of purchases from comments
data['NumBought'] = data['Comment'].str.extract(r'(\d+[Kk]?)\+? bought')[0]
data['NumBought'] = data['NumBought'].replace({'K': '000', 'k': '000'}, regex=True).astype(float)

# Convert Price to numeric by removing dollar sign and commas
data['Price'] = data['Price'].replace('$', '').astype(float)

# Number of Bought vs. Price Scatter Plot
st.scatter_chart(data[['NumBought', 'Price']].dropna())

