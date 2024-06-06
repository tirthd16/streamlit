import streamlit as st
col1, col2 = st.columns(2)
with col1:
    st.title(':blue[Your Competitors Have  Fresh Data—  Do You?]')
    st.markdown("*Stay Current, Stay Competitive*.")
    st.markdown("With our web scraping, fresh data is always at your fingertips. Monthly data refreshes for **lifetime**.")
    st.button('**Contact Now**',type='primary')
    st.button('See Pricing')
with col2:
    st.image("hero.jpg")
st.divider()
