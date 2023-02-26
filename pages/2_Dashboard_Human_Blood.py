import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

st.title("Dashboard - RBC Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "blood.webp")
DATA_PATH = os.path.join(dir_of_interest, "data", "RBC in Humans.csv")



img = image.imread(IMAGE_PATH)
st.image(img)
df = pd.read_csv(DATA_PATH)
age = df['Age']
st.dataframe(df)
col1, col2= st.columns(2)

fig_1 = px.histogram(df[df['Age'] ==age], x="RBC's (in billions)")
col1.plotly_chart(fig_1, use_container_width=True)
fig_2 = px.box(df[df['Age'] == age], y="RBC's (in billions)")
col2.plotly_chart(fig_2, use_container_width=True)


