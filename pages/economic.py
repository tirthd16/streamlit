def stock():
    import streamlit as st
    import pandas as pd
    import altair as alt
    import numpy as np
    st.caption('Economic market information')
    st.download_button('Download sample data',data='mortgage.csv',key='stock')
    tabs1,tabs2 = st.tabs(['Reliance Historical','U.S. Mortgage Rate'])
    with tabs1:
        data = pd.read_csv('csv/stock.csv')  
        arr=['Date','Volume','Close']
        chart_data = data[arr].dropna()
        c = (
           alt.Chart(chart_data)
           .mark_circle()
           .encode(x=arr[0], y=arr[1], size=arr[2],color=arr[2], tooltip=[arr[0], arr[1], arr[2]],
        ))
        st.altair_chart(c, use_container_width=True)
    with tabs2:
        data = pd.read_csv('csv/mortgage.csv')  
        arr=['Release Date','Actual','Previous']
        chart_data = data[arr].dropna()
        c = (
           alt.Chart(chart_data)
           .mark_circle()
           .encode(x=arr[0], y=arr[1], size=arr[2],color=arr[2], tooltip=[arr[0], arr[1], arr[2]],
        ))
        st.altair_chart(c, use_container_width=True)
    if False:
        data = pd.read_csv('csv/mortgage.csv')  
        for cols in data.columns:
            for cols2 in data.columns:
                if cols!=cols2:
                    arr = list(set(["Previous"]+[cols,cols2]))
                    chart_data = data[arr].dropna()
                    c = (
                       alt.Chart(chart_data)
                       .mark_circle()
                       .encode(x=cols, y=cols2, size="Previous",color="Previous", tooltip=[cols, cols2, "Previous"],
                    ))
                    st.altair_chart(c, use_container_width=True)

stock()
