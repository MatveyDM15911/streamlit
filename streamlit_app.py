import streamlit as st

user_id = st.query_params.get("user_id")

if user_id:
    st.success(f"Ваш Telegram user_id: {user_id}")
else:
    st.warning("user_id не найден в параметрах URL")
