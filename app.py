import streamlit as st

 

st.title("Hello, Streamlit!")

st.write("Welcome to your first Streamlit app.")

 

name = st.text_input("What's your name?")

 

# Add a button

if st.button("Click me!"):

    st.write(f"Hello, {name}!")

 

# Add a slider

slider_value = st.slider("Pick a number", min_value=0, max_value=100, value=50)

st.write(f"Slider value: {slider_value}")
