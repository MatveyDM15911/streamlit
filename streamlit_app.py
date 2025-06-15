import streamlit as st
import streamlit.components.v1 as components

# Вставляем JS-код для автоматического и ручного получения user_id
components.html("""
<script src="https://telegram.org/js/telegram-web-app.js"></script>
<script>
function setUserId() {
    if (window.Telegram && window.Telegram.WebApp && window.Telegram.WebApp.initDataUnsafe) {
        let userId = window.Telegram.WebApp.initDataUnsafe.user?.id;
        if (userId) {
            const url = new URL(window.location);
            url.searchParams.set('user_id', userId);
            window.location.replace(url);
        } else {
            alert('user_id не найден. Откройте приложение через Telegram.');
        }
    } else {
        alert('Telegram WebApp не найден. Откройте приложение через Telegram.');
    }
}

// Попытка автоматического получения user_id
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
<button onclick="setUserId()" style="margin-top:10px;">Получить user_id</button>
""", height=60)

user_id = st.query_params.get("user_id")
if not user_id:
    st.warning("Ожидание получения user_id из Telegram... Если не появилось, нажмите кнопку выше.")
    st.stop()
else:
    st.info(f"Ваш Telegram user_id: {user_id}")

# --- Основной функционал приложения ниже ---
import json # Может пригодиться для отправки структурированных данных

st.set_page_config(
    page_title="AI Interaction Mini App",
    layout="centered"
)

st.title("Мой AI-помощник")
st.write("Введите текст или данные для отправки AI.")

user_input = st.text_area(
    "Введите ваш запрос или заметку:",
    height=150,
    key="input_area"
)

if st.button("Отправить AI"):
    if user_input:
        st.write("Вы ввели:")
        st.write(user_input)
        # Здесь может быть отправка данных вашему AI
        st.success("Данные отправлены (имитация)")
    else:
        st.warning("Введите текст перед отправкой!")

note_date = st.date_input("Дата для заметки:")
note_time = st.text_input("Время для заметки:", value="HH:MM")

st.subheader("Последние ответы AI:")
st.text("Здесь могли бы отображаться ответы")
