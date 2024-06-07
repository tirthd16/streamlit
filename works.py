def works():
    import streamlit as st
    import pandas as pd
    import numpy as np
    st.markdown('''
### Demo Dashboards
    ''')
    st.caption('Please note that the data below is from a small sample of our past projects, so it may not be completely reliable.')
    with st.expander('**Computer peripherals market**'):
        import amazon
        amazon.amazon()
    with st.expander('**Real Estate market**'):
        import maharera
        maharera.maharera()
    with st.expander('**Economic Events**'):
        import stock
        stock.stock()
