import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from helper import load_data

st.title("📖 Dataset Details")

df = load_data()

st.write("This dashboard uses **World Happiness Report 2021** data.")

st.markdown("### 🔗 Resources")
st.markdown("- [World Happiness Report](https://worldhappiness.report/)")
st.markdown("- [Dataset on Kaggle](https://www.kaggle.com/unsdsn/world-happiness)")

st.markdown("### 📅 Report History")
timeline = {
    "2012": "First global report published",
    "2015": "Well-being metrics refined",
    "2021": "Focus on COVID-19 impact",
}
for year, event in timeline.items():
    st.write(f"**{year}** → {event}")

st.markdown("### 📊 Dataset Overview")
st.dataframe(df.head())

st.markdown("### 📑 Summary Statistics")
st.write(df.describe())

st.markdown("### 🧩 Missing Values")
fig, ax = plt.subplots(figsize=(8, 4))
sns.heatmap(df.isna(), cbar=False, cmap="viridis")
st.pyplot(fig)

st.markdown("### 📚 Variable Dictionary")
columns_info = {
    "Country name": "Country",
    "Regional indicator": "Region",
    "Life Ladder": "Happiness score (0-10)",
    "Log GDP per capita": "Economic performance",
    "Social support": "Family & community support",
    "Healthy life expectancy at birth": "Expected healthy lifespan",
    "Freedom to make life choices": "Freedom perception",
    "Generosity": "Donations & altruism",
    "Perceptions of corruption": "Trust in government/business",
}
st.table(pd.DataFrame(columns_info.items(), columns=["Column", "Description"]))
