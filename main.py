import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from hero import *
from intro import *
from projects import *
from feature import *
from pricing import *
from works import *
from test import *
# st.logo(image='logo.png')
test()
hero() 
intro() 
projects() 
works()
feature() 
pricing() 
hide_streamlit_style= """<style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
