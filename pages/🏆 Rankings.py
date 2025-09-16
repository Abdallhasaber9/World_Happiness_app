import streamlit as st
import plotly.express as px
from helper import load_data

st.title("🏆 Country Rankings")

df = load_data()

region = st.selectbox("🌍 Select Region", ["All"] + df["Regional indicator"].unique().tolist())
if region != "All":
    df = df[df["Regional indicator"] == region]

N = st.slider("Number of Countries", 5, 20, 10)

st.markdown("### 🥇 Top Countries")
top_df = df.nlargest(N, "Ladder score")
st.dataframe(top_df[["Country name", "Ladder score"]])
fig_top = px.bar(top_df, x="Ladder score", y="Country name", orientation="h", color="Ladder score")
st.plotly_chart(fig_top, use_container_width=True)

st.markdown("### 😢 Bottom Countries")
bottom_df = df.nsmallest(N, "Ladder score")
st.dataframe(bottom_df[["Country name", "Ladder score"]])
fig_bottom = px.bar(bottom_df, x="Ladder score", y="Country name", orientation="h", color="Ladder score")
st.plotly_chart(fig_bottom, use_container_width=True)
