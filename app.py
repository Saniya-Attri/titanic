import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Config
st.set_page_config(page_title="Titanic EDA Dashboard", layout="wide")

# Title
st.title("🚢 Titanic Data Analytics Dashboard")

# Load Data
df = pd.read_csv("cleaned_titanic.csv")

# Show Data
if st.checkbox("Show Raw Data"):
    st.dataframe(df)

# Sidebar Filters
st.sidebar.header("Filter Options")

# Gender Filter
gender = st.sidebar.selectbox("Select Gender", options=df["Sex"].unique())

# Passenger Class Filter
pclass = st.sidebar.selectbox("Select Passenger Class", options=sorted(df["Pclass"].unique()))

# Fare Range Filter
fare_min = float(df["Fare"].min())
fare_max = float(df["Fare"].max())
fare_range = st.sidebar.slider(
    "Select Fare Range",
    min_value=round(fare_min, 2),
    max_value=round(fare_max, 2),
    value=(round(fare_min, 2), round(fare_max, 2))
)

# Age Range Filter
age_min = float(df["Age"].min())
age_max = float(df["Age"].max())
age_range = st.sidebar.slider(
    "Select Age Range",
    min_value=round(age_min, 1),
    max_value=round(age_max, 1),
    value=(round(age_min, 1), round(age_max, 1))
)

# Apply filters
filtered_df = df[
    (d
