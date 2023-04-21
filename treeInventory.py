import pandas as pd
import altair as alt
import streamlit as st
from vega_datasets import data

data = pd.read_csv('https://raw.githubusercontent.com/KatieS-216/TreeData_VT/main/Municipal_Tree_Inventory.csv')

st.set_page_config(page_title="Vermont Tree Inventory", layout="wide", initial_sidebar_state="collapsed")

col1 = st.columns(1)


with col1:
  # CHART 1 - Point Map of Vermont

  # Read in polygons from topojson
  states = alt.topo_feature(data.us_10m.url, feature='states')

  # Vermont map
  states = alt.Chart(states_data).mark_geoshape(
        fill='lightgray',
        stroke='white'
    ).transform_filter((alt.datum.state == 'VT'))
  
  st.altair(states)

  """# US states background
  background = alt.Chart(states).mark_geoshape(
      fill='lightgray',
      stroke='white'
  ).properties(
      width=500,
      height=300
  ).project('albersUsa')

  st.altair_chart(states)"""
