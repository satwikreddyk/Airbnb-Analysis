import streamlit as st

data = pd.read_csv("cleaned_data.csv")

st.title("Airbnb Data Analysis")

selected_property_type = st.selectbox("Select Property Type", df["property_type"].unique())
filtered_data = df[df["property_type"] == selected_property_type]

st.write("Filtered Data:")
st.write(filtered_data)