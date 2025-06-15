import streamlit as st
import streamlit.components.v1 as components

# JS для получения user_id
components.html("""
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<script>
window.onload = function() {
    if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.initDataUnsafe) {
        let userId = window.Telegram.WebApp.initDataUnsafe.user?.id;
        if (userId) {
            const url = new URL(window.location);
            if (!url.searchParams.get('user_id')) {
                url.searchParams.set('user_id', userId);
                window.location.replace(url);
            }
        }
    }
}
</script>
""", height=0)

user_id = st.query_params.get("user_id")
if not user_id:
    st.warning("Ожидание получения user_id из Telegram...")
    st.stop()
else:
    st.info(f"Ваш Telegram user_id: {user_id}")

# Дальше — ваш основной код (форма, кнопки и т.д.)
# ...
