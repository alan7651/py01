import streamlit as st


# Object notation
selected_item = st.sidebar.selectbox(
    "How can we contact you?",
    ["Email", "Home Phone", "Mobile"]
)


# with notation
with st.sidebar:
    radio_value = st.radio(
        "Choose a shipping method",
        ("Standard(5-15 days)", "Express(2-3 days)")
    )

st.write(selected_item, radio_value)
