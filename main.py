import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
hide_st_style = '''
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
'''

st.markdown(hide_st_style, unsafe_allow_html=True)
st.logo(image='logo.png')
col1, col2 = st.columns(2)
with col1:
    st.title(':blue[Your Competitors Have  Fresh Data—  Do You?]')
    st.markdown("We believe success and failure often hinges on having the most accurate information")
    # st.markdown(" Imagine making a crucial business decision with outdated data—how would that impact your confidence and results?")
    st.markdown("That's why we exist: with our web scraping expertise and free monthly data refreshes, you'll always be steps ahead.")
    st.button('**Contact Now**',type='primary')
    st.button('See Pricing')
with col2:
    st.image("banner.jpg")
st.divider()
import hero
import intro
import projects
import feature
import pricing
import cta
