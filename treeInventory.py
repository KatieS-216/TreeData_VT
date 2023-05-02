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
st.subheader("Does location impact the quality of trees in Vermont?")

# MAP - Tree Locations
treemap = pd.DataFrame(
    d,
    columns=['lat', 'lon']).dropna()

st.map(treemap)

#DIVIDER
st.divider()

# BAR - Number of Trees per Town
bar_number = alt.Chart(treedata, title="Number of Trees per Town").mark_bar().encode(
    x='TOWN',
    y= alt.Y('count(OBJECTID)', title="Number of Trees")
  )

st.altair_chart(bar_number)

#DIVIDER
st.divider()

# BAR - GOOD Trees by Town
bar_good = alt.Chart(treedata, title="Number of Good Trees by Town").mark_bar().encode(
    x='TOWN',
    y= alt.Y('count(ConditionID)', title="Count of Good Trees")
  ).transform_filter(
    alt.FieldEqualPredicate(field='ConditionID', equal='GOOD')
).configure_mark(
    color='#1a8747'
)

st.altair_chart(bar_good)

#DIVIDER
st.divider()

# HISTOGRAM - Count of Tree Conditions
hist_condition = alt.Chart(treedata, title="Count of Tree Conditions").mark_bar().encode(
     x='ConditionID',
     y='count()')
    
st.altair_chart(hist_condition)
