import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/KatieS-216/TreeData_VT/main/Municipal_Tree_Inventory.csv', low_memory=False)


st.set_page_config(page_title="Vermont Tree Inventory", layout="wide", initial_sidebar_state="collapsed")

# mapCol = st.columns(1)
# col2, col3= st.columns(2)

d = {'lat': data['X'], 'lon': data['Y']}

trees = pd.DataFrame(
    data = d)

trees.dropna(axis=1, inplace=True)

# with mapCol:
#    st.map(trees)

st.map(trees)
