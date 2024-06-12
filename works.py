def works():
    import streamlit as st
    import pandas as pd
    import numpy as np
    with st.expander('**Computer peripherals market**'):
        import amazon
        amazon.amazon()
    with st.expander('**Real Estate market**'):
        import maharera
        maharera.maharera()
    with st.expander('**Economic Events**'):
        import stock
        stock.stock()
