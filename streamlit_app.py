import streamlit as st
from streamlit_js_eval import streamlit_js_eval

result = streamlit_js_eval(js_expressions="window.Telegram?.WebApp?.initDataUnsafe?.user?.id", key="get_user_id")
st.write(result)
