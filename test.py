import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
data = pd.read_csv('csv/school.csv')  
def test():
    st.text(data.dtypes)
    for cols in data.columns:
        if data[cols].dtype == 'float64' or data[cols].dtype=='int64':
            for cols2 in data.columns:
                if data[cols2].dtype == 'float64' and  cols!=cols2:
                    chart_data = data[[cols,cols2,'State']]
                    c = (
                        alt.Chart(chart_data)
                        .mark_circle()
                        .encode(
                            x=cols,
                            y=cols2,
                            tooltip=[cols, cols2],
                            color='State',
                        )
                    )

                    st.altair_chart(c, use_container_width=True)
