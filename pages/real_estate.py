def maharera():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk
    df = pd.read_csv('csv/mahacord.csv')

    chart_data = df[['lat','lon']]
    latmean = df['lat'].mean()
    lonmean = df['lon'].mean()
    st.caption('Lead Generation project for real estate under construction in Maharashtra')
    st.download_button('Download sample data',data='csv/maharera.csv',key='maha')
    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=latmean,
            longitude=lonmean,
            zoom=5,
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
