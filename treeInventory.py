import pandas as pd
import altair as alt
import streamlit as st

data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')

# data.sample(10)

st.set_page_config(page_title="Titanic Data", layout="wide", initial_sidebar_state="collapsed")

col1, col2, col3 = st.columns(3)


with col1:
  # CHART 1 - HISTOGRAM OF CLASS

  hist_class = alt.Chart(data).mark_bar().encode(
      alt.X("Pclass:Q", bin=True),
      y='count()'
  )

  st.altair_chart(hist_class)

with col2:
  # CHART 2 - SCATTERPLOT OF AGE & FARE

  scatter_age = alt.Chart(data).mark_circle().encode(
      x='Age',
      y='Fare',
      color = 'Survived',
      tooltip = ['Age','Fare','Survived','Name']
  ).interactive()

  st.altair_chart(scatter_age)

with col3:
  # CHART 3 - HISTOGRAM OF FARE

  hist_fare = alt.Chart(data).mark_bar().encode(
      alt.X("Fare:Q", bin=True),
      y='count()'
  )

  st.altair_chart(hist_fare)
