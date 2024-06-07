import streamlit as st
import pandas as pd
import numpy as np
st.divider()
st.markdown('''
### Demo Dashboards
''')
st.caption('Please note that the data below is from a small sample of our past projects, so it may not be completely reliable.')
with st.expander('**Computer peripherals market**'):
    import amazon
with st.expander('**Real Estate market**'):
    import maharera
with st.expander('**Economic Events**'):
    import stock
