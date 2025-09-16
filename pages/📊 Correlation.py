import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from helper import load_data

st.set_page_config(page_title="📊 Correlation Analysis", layout="wide")
st.title("📊 Correlation Analysis")

df = load_data()

numeric_cols = df.select_dtypes(include="number").columns.tolist()
selected_cols = st.multiselect(
    "Select variables for correlation",
    numeric_cols,
    default=numeric_cols
)

if selected_cols:
    corr = df[selected_cols].corr()

    # 🎨 Heatmap options
    st.markdown("### 🔥 Correlation Heatmap")
    cmap = st.selectbox("Select Color Palette", ["coolwarm", "viridis", "plasma", "magma", "crest"], index=0)
    fig_size = st.slider("Heatmap Size", 5, 15, 10)

    # 📊 Draw heatmap
    fig, ax = plt.subplots(figsize=(fig_size, fig_size))
    sns.heatmap(
        corr,
        annot=True,
        cmap=cmap,
        fmt=".2f",
        linewidths=0.5,
        square=True,
        cbar_kws={"shrink": 0.7, "label": "Correlation Strength"},
        ax=ax
    )
    st.pyplot(fig)

    # 📖 Explanation
    st.markdown("### 📝 How to Read the Heatmap")
    st.info("""
    - Values range from **-1 to 1**.  
    - **1 (dark red / yellowish depending on palette)** → strong positive correlation.  
    - **-1 (dark blue / purple)** → strong negative correlation.  
    - **0 (white/light colors)** → no correlation.  
    """)

    # 📋 Strongest correlations
    st.markdown("### 📋 Strongest Correlations")
    flat_corr = (
        corr.unstack()
        .dropna()
        .sort_values(ascending=False)
    )
    flat_corr = flat_corr[flat_corr < 1]  # remove self correlations

    threshold = st.slider("Minimum correlation (absolute)", 0.0, 1.0, 0.5, 0.05)
    strong_corr = flat_corr[flat_corr.abs() >= threshold]

    st.dataframe(
        strong_corr.reset_index().rename(
            columns={"level_0": "Variable 1", "level_1": "Variable 2", 0: "Correlation"}
        ).style.background_gradient(cmap="coolwarm", subset=["Correlation"])
    )

else:
    st.warning("Please select at least one variable.")
