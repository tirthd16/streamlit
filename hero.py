def hero():
    import streamlit as st
    col1, col2 = st.columns(2)
    with col1:
        st.title(':blue[Your Competitors Have  Fresh Data—  Do You?]')
        st.markdown("We believe success and failure often hinges on having the most accurate information")
        # st.markdown(" Imagine making a crucial business decision with outdated data—how would that impact your confidence and results?")
        st.markdown("That's why we exist- with our data extraction expertise and straightforward approach, you'll always have recent and reliable market data.")
        st.button('**Contact Now**',type='primary')
        st.button('See Pricing')
    with col2:
        st.image("banner.jpg")
    st.divider()
