import streamlit as st
import pandas as pd
import numpy as np
st.divider()
st.markdown('''
### Demo Dashboards
''')
st.caption('Note: The data represented below is taken from a small subset of our previous projects. Thus prone to unreliability')
with st.expander('**Test**'):
    st.download_button('Download sample data',data='test')
    import test
with st.expander('**Computer peripherals market**'):
    import amazon
with st.expander('**Medical Professionals**'):
    st.text('asdf')
