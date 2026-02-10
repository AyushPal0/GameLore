import streamlit as st
from dialogue_engine import generate_dialogue

st.title("AI Game Dialogue Engine")

player_input = st.text_input("You:")

if player_input:
    response = generate_dialogue(...)
    st.write(response)
