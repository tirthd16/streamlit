import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
data = pd.read_csv('csv/amazon_data.csv')  

# Number of Bought vs. Sales Scatter Plot

tab1,tab2,tab3 = st.tabs(['Price vs Sales','Rating','Title'])
with tab1:
    chart_data = data[['Price', 'Sales','ReviewCount','sponsored']].dropna()
    c = (
       alt.Chart(chart_data)
       .mark_circle()
       .encode(x="Price", y="Sales", size='ReviewCount', tooltip=["Price", "Sales", 'ReviewCount'],
                color=alt.Color('sponsored', scale=alt.Scale(domain=[False, True], range=['red', 'blue']))
    ))
    st.altair_chart(c, use_container_width=True)
with tab2:
    st.bar_chart(data['Rating'].value_counts().sort_index())
with tab3:
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt

# Generate word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(data['Title'].dropna()))

# Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)
