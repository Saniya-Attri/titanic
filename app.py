import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Titanic Background Image (Full Page)
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stHeader"], [data-testid="stToolbar"] {
    background: rgba(0,0,0,0);
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

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

# Fare Range Slider
fare_min = float(df["Fare"].min())
fare_max = float(df["Fare"].max())
fare_range = st.sidebar.slider(
    "Select Fare Range",
    min_value=round(fare_min, 2),
    max_value=round(fare_max, 2),
    value=(round(fare_min, 2), round(fare_max, 2))
)

# Age Range Slider
age_min = float(df["Age"].min())
age_max = float(df["Age"].max())
age_range = st.sidebar.slider(
    "Select Age Range",
    min_value=round(age_min, 1),
    max_value=round(age_max, 1),
    value=(round(age_min, 1), round(age_max, 1))
)

# Apply Filters
filtered_df = df[
    (df["Sex"] == gender) &
    (df["Pclass"] == pclass) &
    (df["Fare"] >= fare_range[0]) & (df["Fare"] <= fare_range[1]) &
    (df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])
]

# Show filtered data preview
st.subheader("Filtered Data Preview")
st.write(filtered_df.head())

# === Row 1: Survival by Gender and by Class ===
st.subheader("1. Survival Analysis")

col1, col2 = st.columns(2)

with col1:
    fig1, ax1 = plt.subplots()
    fig1.set_size_inches(5, 3)
    sns.countplot(data=filtered_df, x="Survived", hue="Sex", ax=ax1)
    ax1.set_title("Survival by Gender")
    st.pyplot(fig1)

with col2:
    fig2, ax2 = plt.subplots()
    fig2.set_size_inches(5, 3)
    sns.countplot(data=df, x="Pclass", hue="Survived", ax=ax2)
    ax2.set_title("Survival by Class")
    st.pyplot(fig2)

# === Row 2: Age and Fare Distribution ===
st.subheader("2. Distribution Plots")

col3, col4 = st.columns(2)

with col3:
    fig3, ax3 = plt.subplots()
    fig3.set_size_inches(5, 3)
    sns.histplot(data=filtered_df, x="Age", kde=True, bins=30, ax=ax3)
    ax3.set_title("Filtered Age Distribution")
    st.pyplot(fig3)

with col4:
    fig4, ax4 = plt.subplots()
    fig4.set_size_inches(5, 3)
    sns.histplot(data=filtered_df, x="Fare", kde=True, bins=30, ax=ax4)
    ax4.set_title("Filtered Fare Distribution")
    st.pyplot(fig4)

# === Row 3: Age vs Survival and Correlation Heatmap ===
st.subheader("3. Advanced Visualizations")

col5, col6 = st.columns(2)

with col5:
    fig5, ax5 = plt.subplots()
    fig5.set_size_inches(5, 3)
    sns.kdeplot(data=df[df["Survived"] == 1], x="Age", hue="Sex", fill=True, ax=ax5)
    ax5.set_title("Survivors by Age & Gender")
    st.pyplot(fig5)

with col6:
    fig6, ax6 = plt.subplots()
    fig6.set_size_inches(5, 3)
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax6)
    ax6.set_title("Correlation Heatmap")
    st.pyplot(fig6)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit | Titanic Dataset")

