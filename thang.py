import streamlit as st

# Title
st.title("User Information Form")

# Input fields
name = st.text_input("Enter your name")
age = st.number_input("Enter your age", min_value=0, max_value=120, step=1)
city = st.selectbox("Select your city", ["Mumbai", "Delhi", "Chennai"])
points = st.slider("Select points", 0, 100)
skills = st.multiselect("Select your skills", ["Python", "Java", "C++"])

# Submit button
if st.button("Submit"):
    st.subheader("Submitted Information")
    st.table({
        "Field": ["Name", "Age", "City", "Points", "Skills"],
        "Value": [name, age, city, points, ", ".join(skills)]
    })

