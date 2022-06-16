# import necessary packages
import json
import streamlit as st
import geopandas
import matplotlib.pyplot as plt
import geopandas as gpd
import requests
import pandas as pd
import folium
from streamlit_folium import folium_static


def retrieve_polygon(profile_str, long, lat, c_time_str):
    url = "https://api.mapbox.com/isochrone/v1/mapbox/"
    access_token = "pk.eyJ1IjoibmFuY3lwcmVldGhpIiwiYSI6ImNsNDd4cnZrbDA4a20zZHFlbXc0MnphcTMifQ.MfgC-eblFZH1dzGcKB0sVw"
    headers = {'Content-Type': 'application/json'}
    proxies = {"http": None, "https": None}
    point_str = str(long) + "," + str(lat)
    final_url = url + profile_str + "/" + point_str + '?contours_minutes=' + c_time_str + "&contours_colors=6706ce&polygons=true&access_token=" + access_token
    response = requests.request("GET", final_url, headers=headers, proxies=proxies)

    if response.ok:
        print(final_url)
        response_data = json.loads(response.text)
        if response_data:
            print("SUCCESS")
            df = pd.DataFrame(response_data['features'])
            df = df['geometry']  # Series
            df = df[0]  # dict
            # df_coordinates = df['coordinates']
            coord_list = df['coordinates'][0]
            coord_list_df = pd.DataFrame(coord_list, columns=['x', 'y'])
            gdf = geopandas.GeoDataFrame(
                coord_list_df, crs="EPSG:4326", geometry=geopandas.points_from_xy(coord_list_df.x, coord_list_df.y))
            # plot on a map with central point being New York
            print(lat, ", ", long)
            m = folium.Map([lat, long], zoom_start=12)
            folium.GeoJson(gdf).add_to(m)
            # folium.LatLngPopup().add_to(m)
            for ind in coord_list_df.index:
                x1 = coord_list_df['x'][ind]
                y1 = coord_list_df['y'][ind]
                if ind+1 < len(coord_list_df):
                    x2 = coord_list_df['x'][ind+1]
                    y2 = coord_list_df['y'][ind+1]
                    folium.PolyLine(locations=[(x1, y1), (x2, y2)], color="green").add_to(m)
                # folium.PolyLine(locations=[coord_list_df[i], coord_list_df[i + 1]], color="green").add_to(m)
                # add_line_to_map(path_map, [coord_list_df[i], coord_list_df[i + 1]])

            folium_static(m, width=700, height=500)
            # # We can now plot our ``GeoDataFrame``.
            # gdf.plot(color='red')


    else:
        print(final_url)
        print(response.text)


# plot the data using geopandas .plot() method
# fig, ax = plt.subplots(figsize = (10,10))
# universities_gdf.plot(ax=ax)
# plt.show()


st.sidebar.title("Display paths")
submitted = st.sidebar.button("Show Paths")
st.write("**Path Map**")

if submitted:
    universities_gdf = gpd.read_file('./CollegesUniversities/CollegesUniversities.shp')
    universities_gdf['Center_point'] = universities_gdf['geometry'].centroid
    universities_gdf["long"] = universities_gdf.Center_point.map(lambda p: p.x)
    universities_gdf["lat"] = universities_gdf.Center_point.map(lambda p: p.y)
    i = 7000
    lat = universities_gdf["lat"][i]
    long = universities_gdf["long"][i]
    print(lat, ", ", long)
    # coord_string = str(universities_gdf["long"][i]) +","+ str(universities_gdf["lat"][i])
    retrieve_polygon("driving", long, lat, "10")

# "https://api.mapbox.com/isochrone/v1/mapbox/driving/-157.8414042476079,21.293023736556165?contours_minutes=5,10,15&contours_colors=6706ce,04e813,4286f4&polygons=true&access_token=pk.eyJ1IjoibmFuY3lwcmVldGhpIiwiYSI6ImNsNDd4cnZrbDA4a20zZHFlbXc0MnphcTMifQ.MfgC-eblFZH1dzGcKB0sVw"
