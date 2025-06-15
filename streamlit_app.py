import streamlit as st

user_id = st.query_params["user_id"]

st.write(user_id)
