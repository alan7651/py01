import streamlit as st

with st.sidebar:
    with st.form("preference"):
        selected_item = st.selectbox(
            "How can we contact you?",
            ("Email", "Home Phone", "Mobile")  # tuple / list
        )

        radio_value = st.radio(
            "Shipping method",
            ("Standard (5- 15 DAYS)", "** Express (2-3 DAYS)")  # tuple / list
        )

        st.form_submit_button("確認")


st.write("聯絡方式: By ", selected_item, "運送方式: ", radio_value)
