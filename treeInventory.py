import pandas as pd
import altair as alt
from pyproj import Transformer
import streamlit as st
# from vega_datasets import data

treedata = pd.read_csv('https://raw.githubusercontent.com/KatieS-216/TreeData_VT/main/Municipal_Tree_Inventory.csv', low_memory=False)

# mapCol = st.columns(1)
col2, col3= st.columns(2)

transf = Transformer.from_crs( "epsg:3684","epsg:4326",always_xy=False)

x1, y1 = transf.transform(treedata['X'], treedata['Y'])

d = {'lat': x1, 'lon': y1}

alt.data_transformers.disable_max_rows()

"""
# MAP

# Read trees in points
trees = pd.DataFrame(d)

# Read in polygons from topojson
states_data = alt.topo_feature(data.us_10m.url, feature='states')

# US states background
states = alt.Chart(states_data).mark_geoshape(
    fill='lightgray',
    stroke='white'
).project('albersUsa'
).transform_filter((alt.datum.id == '22'))

# tree positions on background
points = alt.Chart(trees).mark_circle(
    size=10,
    color='steelblue'
).encode(
    longitude='lat:Q',
    latitude='lon:Q',
    #tooltip
)

states + points
"""

with col2:
    alt.Chart(treedata).mark_bar().encode(
    x=data['ConditionID'],
    y='count()')

st.altair_chart(Chart)
