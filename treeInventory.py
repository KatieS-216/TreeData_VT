import pandas as pd
import altair as alt
from pyproj import Transformer
import streamlit as st
import numpy as np

# IMPORT TREE DATA
treedata = pd.read_csv('https://raw.githubusercontent.com/KatieS-216/TreeData_VT/main/Municipal_Tree_Inventory.csv', low_memory=False)


# CONVERT COORDINATES
transf = Transformer.from_crs( "epsg:3684","epsg:4326",always_xy=False)

x1, y1 = transf.transform(treedata['X'], treedata['Y'])

d = {'lat': x1, 'lon': y1}

alt.data_transformers.disable_max_rows()

# USE CUSTOM MAP TOKEN
token = 'pk.eyJ1Ijoia2F0aWUtcy0yMTYiLCJhIjoiY2xoNWhrdjdwMDE1OTNkcDUwMDZ0b3hqYiJ9.kov77lplpJ-rqzlQeExusw'

# TITLE
st.title('Vermont Tree Inventory')

# MAP - Tree Locations
treemap = pd.DataFrame(
    d,
    columns=['lat', 'lon']).dropna()

st.map(treemap)

# HISTOGRAM - Count of Tree Conditions
hist_condition = alt.Chart(treedata).mark_bar().encode(
     alt.X("Condition:Q", bin=True),
     y='count')
    
st.altair_chart(hist_class)
