from pandas._libs import index


def amazon():
    import streamlit as st
    import pandas as pd
    import altair as alt
    import numpy as np
    data = pd.read_csv('csv/amazon_data.csv')  
    @st.cache_data
    def convert_df(data):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return data.to_csv(index=False).encode("utf-8")

    csv = convert_df(data)

# Number of Bought vs. Sales Scatter Plot

    st.caption('Data from amazon and flipkart for insights on computer peripherals market')
    st.download_button('Download sample data',data=csv,key='amazon', mime='csv', file_name='amazon_sample.csv')
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
#    from wordcloud import WordCloud
#    import matplotlib.pyplot as plt
#    import streamlit as st  # Assuming you're using Streamlit for display
#
## Generate word cloud with dark background and light text
#    wordcloud = WordCloud(
#        width=800,
#        height=400,
#        background_color='black',  # Dark background
#        colormap='Pastel1'         # Light color map for words
#    ).generate(' '.join(data['Title'].dropna()))
#
## Display the word cloud
#    plt.figure(figsize=(10, 5))
#    plt.imshow(wordcloud, interpolation='bilinear')
#    plt.axis('off')
#    plt.gca().set_facecolor('black')  # Set figure background color to dark
#    st.pyplot(plt)
#
        st.text('pending')
amazon()
