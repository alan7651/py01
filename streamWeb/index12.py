import streamlit as st

st.title("計數器範例")
# count = 0

# 檢查 st.session_state 是否已有 'count'
# 重新整理 st.session_state 會被清空
if 'count' not in st.session_state:
    st.session_state['count'] = 0

# 若button 指定key 則會在sesosn_state 中建立 key值 (可不指定)
increment_pressed = st.button("✚1", key="Key_has_pressed")

if increment_pressed:
    st.session_state['count'] += 1

st.write("Count: ", st.session_state.count)

# 新增session_state 檢視區塊
st.divider()
st.caption("session_state:")
st.session_state
