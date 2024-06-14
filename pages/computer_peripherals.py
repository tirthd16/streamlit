def amazon():
    from collections import Counter
    import matplotlib.pyplot as plt
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
    tab2,tab3,tab1 = st.tabs(['Keyword Analysis','Avg sales for sponsored','Price vs Sales'])
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
# Download stopwords from nltk
        data['Revenue'] = data['Sales'] * data['Price']


        titles = data['Title'].dropna().tolist()
        stop_words= {'for', 'with', 'and', '-', '&', 'Mouse,'}
        words = ' '.join(titles).split()
        filtered_words = [word for word in words if word not in stop_words]
        common_words = Counter(filtered_words).most_common(20)  # Get the 20 most common words

        st.header('Revenue Analysis')
        total_revenue = data['Revenue'].sum()
        st.write(f'Total Revenue: ${total_revenue:,.2f}')

# Display common keywords
        st.header('Common Keywords in Titles')
        for word, count in common_words:
            st.write(f'{word}: {count}')

# Calculate revenue

# Plot revenue by keyword
        st.header('Revenue by Keyword')
        keyword_revenue = {}
        for word, count in common_words:
            keyword_revenue[word] = data[data['Title'].str.contains(word, na=False)]['Revenue'].sum()

# Display the keyword revenue

        keyword_revenue_df = pd.DataFrame.from_dict(keyword_revenue, orient='index', columns=['Revenue']).sort_values(by='Revenue', ascending=False)

# Plot the bar chart using Streamlit
        st.bar_chart(keyword_revenue_df['Revenue'])

        c= alt.Chart(keyword_revenue_df).mark_bar().encode(
                x='Keyword',
                y='Revenue')

        #st.altair_chart(c, use_container_width=True)



    with tab3:
        grouped_df = data.groupby(['Rating', 'sponsored']).agg({'Sales': 'mean'}).reset_index()

# Separate the data into sponsored and non-sponsored
        sponsored_true = grouped_df[grouped_df['sponsored'] == True]
        sponsored_false = grouped_df[grouped_df['sponsored'] == False]

# Calculate average sales for combined sponsored and non-sponsored
        combined_df = data.groupby('Rating').agg({'Sales': 'mean'}).reset_index()

# Plotting
        fig, ax = plt.subplots(figsize=(10, 6))
        fig.patch.set_facecolor('#2E2E2E')
        ax.set_facecolor('#2E2E2E')

# Plot sponsored true line
        ax.plot(sponsored_true['Rating'], sponsored_true['Sales'], label='Sponsored', marker='o', color='#1f77b4')

# Plot sponsored false line
        ax.plot(sponsored_false['Rating'], sponsored_false['Sales'], label='Not Sponsored', marker='o', color='#ff7f0e')

# Plot combined line
        ax.plot(combined_df['Rating'], combined_df['Sales'], label='Combined', marker='o', linestyle='--', color='#2ca02c')

# Add labels and title with light color
        ax.set_xlabel('Rating', color='white')
        ax.set_ylabel('Average Sales per month', color='white')

# Set the tick parameters to white
        ax.tick_params(axis='both', colors='white')

# Set the legend with light color
        legend = ax.legend()
        st.pyplot(fig)
amazon()

