
def school():
    import streamlit as st
    import pandas as pd
    import altair as alt
    import numpy as np
    data = pd.read_csv('csv/school.csv')  

# Number of Bought vs. College Readiness Scatter Plot

    st.caption('Benchmarks and demographics for schools across USA')
    st.download_button('Download sample data',data='csv/school.csv',key='def')
    tab1,tab2 = st.tabs(['rank vs College Readiness','Student-Teacher Ratio'])
    with tab1:
        chart_data = data[['rank', 'College Readiness','State']].dropna()
        c = (
           alt.Chart(chart_data)
           .mark_circle()
           .encode(x="rank", y="College Readiness", tooltip=["rank", "College Readiness", 'State'], color='State'
        ))
        st.altair_chart(c, use_container_width=True)
    with tab2:
        st.bar_chart(data['Student-Teacher Ratio'].value_counts().sort_index())
school()
