import pandas as pd
import altair as alt
import streamlit as st
from pyproj import Transformer

data = pd.read_csv('https://raw.githubusercontent.com/KatieS-216/TreeData_VT/main/Municipal_Tree_Inventory.csv', low_memory=False)


st.set_page_config(page_title="Vermont Tree Inventory", layout="wide", initial_sidebar_state="collapsed")

# mapCol = st.columns(1)
# col2, col3= st.columns(2)

transf = Transformer.from_crs( "epsg:3684","epsg:4326",always_xy=False)

x1, y1 = transf.transform(data['X'], data['Y'])

#print(x1, y1)

d = {'lat': x1, 'lon': y1}
trees = pd.DataFrame(data=d, dtype=float64)

#trees.dropna(axis=1, inplace=True)

# with mapCol:
st.map(trees)

#data['Y'].sample(10)
