import streamlit as st

params = st.query_params()
user_id = params.get("user_id", [None])[0]

if user_id:
    st.success(f"Ваш Telegram user_id: {user_id}")
else:
    st.warning("user_id не найден в параметрах URL")
