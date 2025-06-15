import streamlit as st
from streamlit_js_eval import streamlit_js_eval

result = streamlit_js_eval(js_expressions="window.Telegram?.WebApp?.initDataUnsafe", key="get_init_data")
st.write("initDataUnsafe:", result)
