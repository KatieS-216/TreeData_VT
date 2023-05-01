import pandas as pd
import altair as alt
from pyproj import Transformer
import streamlit as st
import numpy as np
# from vega_datasets import data

treedata = pd.read_csv('https://raw.githubusercontent.com/KatieS-216/TreeData_VT/main/Municipal_Tree_Inventory.csv', low_memory=False)

# mapCol = st.columns(1)
#col2, col3= st.columns(2)

transf = Transformer.from_crs( "epsg:3684","epsg:4326",always_xy=False)

x1, y1 = transf.transform(treedata['X'], treedata['Y'])

d = {'lat': x1, 'lon': y1}

# alt.data_transformers.disable_max_rows()

token = 'pk.eyJ1Ijoia2F0aWUtcy0yMTYiLCJhIjoiY2xoNWhrdjdwMDE1OTNkcDUwMDZ0b3hqYiJ9.kov77lplpJ-rqzlQeExusw'

treemap = pd.DataFrame(
    d,
    columns=['lat', 'lon'])

st.map(treemap)

# treemap = pd.Dataframe(columns= [d['lat'], d['lon']])
# st.map(treemap)
