def doctors():
    import streamlit as st
    import pandas as pd
    st.set_page_config(initial_sidebar_state="collapsed")
    st.markdown(
        """
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
    df = pd.read_csv('csv/doctor.csv')
    @st.cache_data
    def convert_df(data):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return data.to_csv(index=False).encode("utf-8")

    csv = convert_df(df)
    st.caption('Lead generation of primary care NYC doctors with contact and address')
    st.download_button('Download sample data',data=csv,key='doctor', file_name="NY_doctors.csv", mime='csv')
    st.dataframe(df, hide_index=True)

doctors()
