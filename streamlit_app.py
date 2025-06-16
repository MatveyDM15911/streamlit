# --- Инициализация всех ключей st.session_state в одном месте ---
# Это гарантирует, что они существуют до первого использования
if "redis_manager" not in st.session_state:
    st.session_state.redis_manager = RedisHistoryManager()

if "all_chat_names" not in st.session_state:
    st.session_state.all_chat_names = st.session_state.redis_manager.get_all_chat_names(user_id)

if "current_chat_name" not in st.session_state:
    if not st.session_state.all_chat_names:
        st.session_state.current_chat_name = DEFAULT_CHAT_NAME
    else:
        st.session_state.current_chat_name = st.session_state.all_chat_names[0]

# is_first_message должен быть инициализирован до того, как его будут использовать
if "is_first_message" not in st.session_state:
    # Определяем, является ли чат новым/пустым на основе загруженной истории
    # (если current_chat_name уже определен)
    if st.session_state.current_chat_name == DEFAULT_CHAT_NAME:
        st.session_state.is_first_message = True
    else:
        loaded_initial_history = st.session_state.redis_manager.load_chat_history(user_id, st.session_state.current_chat_name)
        st.session_state.is_first_message = not bool(loaded_initial_history)

if "messages" not in st.session_state:
    st.session_state.messages = []
