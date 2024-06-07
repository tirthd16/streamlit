import streamlit as st
st.divider()
st.markdown('## Pricing')
col1,col2,col3 = st.columns(3)
with col1:
    with st.container(border=True):
        st.markdown('#### 75\$ - 200$')
        st.markdown('#### ₹6K - ₹15K')
        st.divider()
        st.markdown('**<10K** rows')
        st.markdown('**<7** columns')
        st.markdown('**<3** sources of data')
        st.divider()
        st.markdown('~3 days delivery')
        st.markdown('Free online dashboard')
        st.markdown('Free monthly data updates')
with col2:
    with st.container(border=True):
        st.markdown('#### 200\$ - 400$')
        st.markdown('#### ₹15K - ₹30K')
        st.divider()
        st.markdown('**<30K** rows')
        st.markdown('**<15** columns')
        st.markdown('**<5** sources of data')
        st.divider()
        st.markdown('7 days delivery')
        st.markdown('Free online dashboard')
        st.markdown('Free monthly data updates')
with col3:
    with st.container(border=True):
        st.markdown('#### Custom Pricing')
        st.divider()
        st.markdown('For more extensive needs')
        st.divider()
        st.markdown('Priority support')
        st.markdown('Free online dashboard')
        st.markdown('Free monthly data updates')
