import streamlit as st
import plotly.express as px
from helper import load_data

st.title("📈 Interactive Data Exploration")

df = load_data()

x_var = st.selectbox("📌 Select X-axis", df.select_dtypes(include="number").columns)
y_var = st.selectbox("📌 Select Y-axis", df.select_dtypes(include="number").columns, index=1)
size_var = st.selectbox("⭕ Bubble Size", [None] + df.select_dtypes(include="number").columns.tolist())
color_var = st.selectbox("🎨 Color By", [None, "Regional indicator"])

st.markdown("### 📊 Scatter Plot")
fig = px.scatter(df, x=x_var, y=y_var, size=size_var, color=color_var,
                 hover_name="Country name")
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📊 Line Plot")
fig_line = px.line(df.sort_values(x_var), x=x_var, y=y_var, color="Regional indicator")
st.plotly_chart(fig_line, use_container_width=True)
