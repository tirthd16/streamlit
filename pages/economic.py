def stock():
    import streamlit as st
    import pandas as pd
    import altair as alt
    import numpy as np
    st.set_page_config(initial_sidebar_state="collapsed")
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    data = pd.read_csv('csv/stock.csv')  
    data2 = pd.read_csv('csv/mortgage.csv')  
    @st.cache_data
    def convert_df(data):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return data.to_csv(index=False).encode("utf-8")

    csv = convert_df(data)
    csv2 = convert_df(data2)
    st.caption('Economic market information')
    st.download_button('Download sample data',data=csv2,key='stock', file_name="economic_market_sample.csv", mime='csv')
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
