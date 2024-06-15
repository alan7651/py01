import streamlit as st
import time

placeholder = st.empty()

with placeholder:
    total_sec = 0
    for each_second in range(5):
        st.write(f"{each_second} seconds have passed")
        time.sleep(1)
        total_sec += 1

    st.write(f"🥳 {total_sec} seconds is over!")

time.sleep(5)
placeholder.empty()
