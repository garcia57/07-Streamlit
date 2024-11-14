import streamlit as st

# Prompt the user to enter a name
input_name = st.text_input('Enter a name:')

# Display the entered name
if input_name:
    st.write(f'Hello, {input_name}!')
