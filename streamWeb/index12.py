import streamlit as st

st.title("計數器範例")
count = 0

if 'count' not in st.session_state:
    st.session_state['count'] = 0

increment_pressed = st.button("加1")

if increment_pressed:
    st.session_state['count'] += 1

st.write("Count: ", st.session_state.count)
