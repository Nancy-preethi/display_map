import math

import folium
import streamlit as st
from geopy.geocoders import google
from streamlit_folium import folium_static

st.sidebar.title("Display paths")

submitted = st.sidebar.button("Show Paths")


def arrow_points_calculate(ini_lat, ini_long, heading):
    lenght_scale = 0.000012
    sides_scale = 0.0008
    sides_angle = 25

    latA= ini_lat
    longA = ini_long

    latB = lenght_scale * math.cos(math.radians(heading)) + latA
    longB = lenght_scale * math.sin(math.radians(heading)) + longA

    latC = sides_scale * math.cos(math.radians(heading + 180 - sides_angle)) + latB
    longC = sides_scale * math.sin(math.radians(heading + 180 - sides_angle)) + longB

    latD = sides_scale * math.cos(math.radians(heading + 180 + sides_angle)) + latB
    longD = sides_scale * math.sin(math.radians(heading + 180 + sides_angle)) + longB

    pointA = (latA, longA)
    pointB = (latB, longB)
    pointC = (latC, longC)
    pointD = (latD, longD)

    point = [pointA, pointB, pointC, pointD, pointB]
    return point

if submitted:
    path_map = folium.Map(location=[11.00920925,76.9599098], zoom_start=14, width="%100", height="%100")

    st.write("**Path Map**")
    folium.Marker(location=[42.044, -92.830], popup="start", icon=folium.Icon(color='blue', icon='ok-sign'), ).add_to(
        path_map)
    # points = arrow_points_calculate(42.044, -92.830, -92.830)
    folium.PolyLine(locations=[(11.00920925,76.9599098), (11.0270976,76.95202002)], color="purple").add_to(
        path_map)


    folium.Marker(location=[44.044, -92.830], popup="start", icon=folium.Icon(color='blue', icon='ok-sign'), ).add_to(
        path_map)
    points = arrow_points_calculate((11.0270976+11.00920925)/2,(76.9599098 + 76.95202002)/2, -11.04)
    folium.PolyLine(locations=points, color="purple").add_to(path_map)





    folium_static(path_map, width=700, height=500)
