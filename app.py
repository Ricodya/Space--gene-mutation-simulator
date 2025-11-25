
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Space Mutation Simulator", layout="wide")

st.title("🚀 Space Mutation Simulator")

days = st.slider("Days in Space", 30, 1095, 180)
gene = st.selectbox("Select Gene", ["TP53", "BRCA1", "TERT", "MT-RNR1"])

df = pd.read_csv("space_mutation_dataset.csv")

st.subheader("Radiation Over Time")
fig = px.line(df.head(days), x="date", y="radiation_mGy_day")
st.plotly_chart(fig, use_container_width=True)

st.download_button(
    label="📥 Download Dataset",
    data=open("space_mutation_dataset.csv", "rb").read(),
    file_name="space_mutation_dataset.csv"
)

st.success("✅ Streamlit App Ready!")
