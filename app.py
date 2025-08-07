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
gender = st.sidebar.selectbox("Select Gender", options=df["Sex"].unique())
pclass = st.sidebar.selectbox("Select Passenger Class", options=df["Pclass"].unique())

# Apply filters
filtered_df = df[(df["Sex"] == gender) & (df["Pclass"] == pclass)]

st.subheader("Filtered Data Preview")
st.write(filtered_df.head())

# 1. Survival Count by Gender
st.subheader("1. Survival Count by Gender")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x="Survived", hue="Sex", ax=ax1)
ax1.set_title("Survival Distribution by Gender")
st.pyplot(fig1)

# 2. Survival Rate by Passenger Class
st.subheader("2. Survival Count by Passenger Class")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x="Pclass", hue="Survived", ax=ax2)
ax2.set_title("Survival by Passenger Class")
st.pyplot(fig2)

# 3. Age Distribution
st.subheader("3. Age Distribution")
fig3, ax3 = plt.subplots()
sns.histplot(data=df, x="Age", kde=True, bins=30, ax=ax3)
ax3.set_title("Distribution of Passenger Ages")
st.pyplot(fig3)

# 4. Fare Distribution by Class
st.subheader("4. Fare Distribution by Class")
fig4, ax4 = plt.subplots()
sns.boxplot(data=df, x="Pclass", y="Fare", ax=ax4)
ax4.set_title("Fare Distribution across Passenger Classes")
st.pyplot(fig4)

# 5. Survival Rate by Age and Gender
st.subheader("5. Survival by Age and Gender")
fig5, ax5 = plt.subplots()
sns.kdeplot(data=df[df["Survived"] == 1], x="Age", hue="Sex", fill=True, ax=ax5)
ax5.set_title("Survivors by Age and Gender")
st.pyplot(fig5)

# 6. Heatmap of Correlations
st.subheader("6. Correlation Heatmap")
fig6, ax6 = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", ax=ax6)
ax6.set_title("Feature Correlation Matrix")
st.pyplot(fig6)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Streamlit | Titanic Dataset")
