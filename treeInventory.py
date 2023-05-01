import pandas as pd
import altair as alt
import streamlit as st
import numpy as np
from pyproj import Transformer

data = pd.read_csv('https://raw.githubusercontent.com/KatieS-216/TreeData_VT/main/Municipal_Tree_Inventory.csv', low_memory=False)


st.set_page_config(page_title="Vermont Tree Inventory", layout="wide", initial_sidebar_state="collapsed")

# mapCol = st.columns(1)
# col2, col3= st.columns(2)

transf = Transformer.from_crs( "epsg:3684","epsg:4326",always_xy=False)

x1, y1 = transf.transform(data['X'], data['Y'])

#d = {'lat': x1, 'lon': y1}

"""lat = x1
lon = y1

trees = pd.DataFrame(columns=['lat','lon'])

st.map(trees)"""

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(df)
