def maharera():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk
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
    df = pd.read_csv('csv/mahacord.csv')
    df2 = pd.read_csv('csv/maharera.csv')
    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index=False).encode("utf-8")

    csv = convert_df(df2)

    chart_data = df[['lat','lon']]
    latmean = df['lat'].mean()
    lonmean = df['lon'].mean()
    st.caption('Lead Generation project for real estate under construction in Maharashtra')
    st.download_button('Download sample data',data=csv,key='maha', file_name='real_estate.csv', mime='csv')
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=latmean-0.8,
            longitude=lonmean-1.8,
            zoom=8,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HexagonLayer',
               data=chart_data,
               get_position='[lon, lat]',
               radius=200,
               elevation_scale=4,
               elevation_range=[0, 1000],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))
maharera()
