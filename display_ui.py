import folium
import streamlit as st
from streamlit_folium import folium_static

st.sidebar.title("Display paths")

submitted = st.sidebar.button("Show Paths")
if submitted:
    path_map = folium.Map(location=[42.044, -92.830], zoom_start=10, width="%100", height="%100")

    st.write("**Path Map**")
    folium.Marker(location=[42.044, -92.830], popup="start", icon=folium.Icon(color='blue', icon='ok-sign'), ).add_to(
        path_map)
    folium_static(path_map, width=700, height=500)
