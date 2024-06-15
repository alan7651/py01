import streamlit as st
import time

placeholder = st.empty()

with placeholder:
    for each_second in range(5):
        st.write(f"{each_second} seconds have passed")
        time.sleep(1)

    st.write("🥳 1 minute over!")

time.sleep(5)
placeholder.empty()
