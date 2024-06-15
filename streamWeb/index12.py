import streamlit as st

st.title("計數器範例")
# count = 0

# 檢查 st.session_state 是否已有 'count'
if 'count' not in st.session_state:
    st.session_state['count'] = 0

increment_pressed = st.button("✚1")

if increment_pressed:
    st.session_state['count'] += 1

st.write("Count: ", st.session_state.count)
