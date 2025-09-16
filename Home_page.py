import streamlit as st
import plotly.express as px
from helper import load_data

st.set_page_config(page_title="🏠 World Happiness Dashboard", layout="wide")

st.title("🏠 World Happiness Dashboard")

df = load_data()

col1, col2, col3 = st.columns(3)
col1.metric("🌍 Number of Countries", df["Country name"].nunique())
col2.metric("😊 Average Happiness", round(df["Ladder score"].mean(), 2))
col3.metric("🥇 Happiest Country", df.loc[df["Ladder score"].idxmax(), "Country name"])

st.markdown("### 🌎 Global Happiness Map")
fig_map = px.scatter_geo(
    df,
    locations="Country name",
    locationmode="country names",
    color="Ladder score",
    hover_name="Country name",
    size="Ladder score",
    projection="natural earth"
)
st.plotly_chart(fig_map, use_container_width=True)

st.markdown("### 📦 Happiness Distribution by Region")
fig_box = px.box(df, x="Regional indicator", y="Ladder score", color="Regional indicator")
st.plotly_chart(fig_box, use_container_width=True)

fig_map = px.scatter_geo(df, locations="Country name", locationmode="country names",
                         color="Ladder score", hover_name="Country name",
                         size="Ladder score", projection="natural earth")
