import streamlit as st

with st.form("my_form"):
    st.write("Inside the form")
    slide_value = st.slider("請選擇滿意度 0-100")  # 可指定min & max
    checkbox_value = st.checkbox("同意使用條款")

    # 追蹤提交狀態
    submitted = st.form_submit_button(label="提交", use_container_width=True)


if submitted:
    st.write("表單回應:")
    # 若沒slider 與 check box 沒有寫在form內，則變更值時會直接改寫st.write內容
    # 寫在form 裡面一定要submit 按鈕提交後 slide_value 與 checkbox_value才會顯示值
    st.write("滿意度", slide_value, "是否同意條款", checkbox_value)
