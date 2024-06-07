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
import hero
import intro
import projects
import feature
import pricing
import cta
