import streamlit as st

user_id = st.query_params.get()

st.write(user_id)
