import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")


col1, col2 = st.columns(2)


with col1:
    st.image("images/ohm.jpg")

with col2:
    st.title("Viphava Khlaisuwan (Ohm)")

    content = """My name is Viphava Khlaisuwan, a third-year Software Engineering student at Thammasat University with an outstanding 
    GPA of 3.94/4.00. My academic journey is enriched with coursework in Data Science, Machine Learning, and 
    Programming, complemented by practical experiences like my role as a Research Assistant at CILS Lab, where I worked on 
    image processing and dataset preparation using YOLOv8. I have also engaged in project work, notably in Dental Detection and sleep state analysis, and contributed as a Technical Core Team Member in the Google Developer Student Club. My academic excellence is recognized through consecutive Top Academic Excellence Awards and a merit scholarship. Passionate about software engineering and data science, I am driven to apply my skills in creating innovative solutions.

"""
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

df = pd.read_csv("data.csv", sep=";")
with col3:
    for index, row in df.iterrows():
        if index % 2 == 0:
            st.header(row['title'])
            st.image(f'images/{row["image"]}')

with col4:
    for index, row in df.iterrows():
        if index % 2 != 0:
            st.header(row['title'])
            st.image(f'images/{row["image"]}')