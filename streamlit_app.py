import streamlit as st
from streamlit_js_eval import streamlit_js_eval

result = streamlit_js_eval(js_expressions="window.Telegram?.WebApp?.initDataUnsafe?.user?.id", key="get_user_id")
user_id = result["data"]

if user_id:
    st.success(f"Ваш Telegram user_id: {user_id}")
else:
    st.info("Откройте приложение через Telegram Mini App")
